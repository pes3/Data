

--sets controls on how to handle comparison operators

SET ANSI_NULLS ON
GO

---Identifiers can be delimited by double quotation marks, and literals must be delimited by single quotation marks

SET QUOTED_IDENTIFIER ON
GO

USE [demoDW]
GO

CREATE OR ALTER PROCEDURE LOADER_STATE_D AS
BEGIN

	-- LOAD STATE_D

	BEGIN
	
	---Create date range variables so we can perfrom delta loads after first load
	
	
	---Then create audit/control variables
	

	
	---variables to hold column information, one from app DB, the other 
	---for a matching row in DWH, incase of insert those are staying null, but if
	---try to run comparison to see if we need to update existing row then they are populated
	---view logic in loader below
	
		DECLARE @CHECKPOINT DATETIME, @NEWCHECKPOINT DATETIME
		DECLARE @SOURCE_COLUMNS INT, @ROWS_INS INT, @ROWS_DEL INT, @ROWS_UPD INT, @ROWS_SKIP INT
		DECLARE @STATE_D_ID INT, @STATEPROVINCEID INT, @STATEPROVINCECODE NVARCHAR(5), 
			@STATEPROVINCENAME NVARCHAR(50), @SALESTERRITORY NVARCHAR(50)
		DECLARE @N_STATEPROVINCECODE NVARCHAR(5), @N_STATEPROVINCENAME NVARCHAR(50), 
			@N_SALESTERRITORY NVARCHAR(50)

		
		
		--get a value for checkpoint varibale, so we run
		--query out of runs table, if no row available we set a date to an old date
		--whichver is bigger we set our checkpoint.
		--On initial load we pull the wayback date 
		--future loads use last date of run
		--then initials rest of variables
		
		SELECT
			@CHECKPOINT = a.RUN_DT
		FROM
			(
				SELECT 
					MAX(b.RUN_DT) RUN_DT
				FROM
					(
						SELECT RUN_DT FROM [dbo].[RUNS] WHERE RUN_NAME = 'STATE_D'
						UNION
						SELECT CONVERT([datetime],'1990-01-01 00:00:00') RUN_DT
					)b
			) a

		SELECT @NEWCHECKPOINT = GETDATE(), @SOURCE_COLUMNS = 0, @ROWS_INS = 0, @ROWS_DEL = 0, @ROWS_UPD = 0, @ROWS_SKIP = 0

		IF @CHECKPOINT = NULL
		BEGIN
			SET @CHECKPOINT = CONVERT([datetime],'1990-01-01 00:00:00')
		END
		
		--Set up a cursor
		--- a cursor takes a query and allows us to iterate over results table 1 row at a time
		---open a cursor, fetch the first row into variables
		---columns need to have matching variables for fetch to work 
		
		DECLARE DB_CURSOR CURSOR FOR
			SELECT
				STATEPROVINCEID
				, STATEPROVINCECODE
				, STATEPROVINCENAME
				, SALESTERRITORY
			FROM
				WideWorldImporters.[Application].StateProvinces
			FOR SYSTEM_TIME
				BETWEEN @CHECKPOINT AND @NEWCHECKPOINT
			ORDER BY
				STATEPROVINCEID, VALIDFROM

		OPEN DB_CURSOR
		FETCH NEXT FROM DB_CURSOR INTO @STATEPROVINCEID, @STATEPROVINCECODE, @STATEPROVINCENAME, @SALESTERRITORY
		
		--set up a while look to trigger 
		--when logic below is not true we have reached the last row
		
		WHILE @@FETCH_STATUS = 0
		BEGIN
		
		--Below we will increment our source columns audit control
		--- this lets us know whe have read a row
		
			SET @SOURCE_COLUMNS = @SOURCE_COLUMNS + 1
			
			--Then we check based on source ID from application DB,
			--which is stored in STATE_SRC_ID,
			--to see if source data is present i DWH. 
			--If it does not exist we perfrom an insert of row into 
			--DWH.
			
			IF NOT EXISTS (SELECT STATE_D_ID FROM STATE_D WHERE STATE_SRC_ID = @STATEPROVINCEID)
			BEGIN

				SET @ROWS_INS = @ROWS_INS + 1
			
				INSERT INTO STATE_D (STATE_SRC_ID, STATE_CODE, STATE_NAME, SALES_TERRITORY) 
					VALUES (@STATEPROVINCEID, @STATEPROVINCECODE, @STATEPROVINCENAME, @SALESTERRITORY)

			END
			ELSE
			BEGIN
			
			--If it did exist, select the row into variables
			--& compare for any difference
			----> if your variables support you could do MD5 hash( look into) and would 
			--need to do on both sides of data,, in this case we cannot do this on application side
			------>look more into if applicable
			
				SELECT
					@N_STATEPROVINCECODE = STATE_CODE
					, @N_STATEPROVINCENAME = STATE_NAME
					, @N_SALESTERRITORY = SALES_TERRITORY
				FROM
					STATE_D
				WHERE
					STATE_SRC_ID = @STATEPROVINCEID

				IF @N_STATEPROVINCECODE <> @STATEPROVINCECODE OR @N_STATEPROVINCENAME <> @STATEPROVINCENAME OR @N_SALESTERRITORY <> @SALESTERRITORY
				BEGIN

					SET @ROWS_UPD = @ROWS_UPD + 1
					
--					If we do find a discrepencies between values, we need to perfrom increment to our update
--perfrom update, and makesure you update the update date

					UPDATE
						STATE_D
					SET
						STATE_CODE = @STATEPROVINCECODE
						, STATE_NAME = @STATEPROVINCENAME
						, SALES_TERRITORY = @SALESTERRITORY
						, LAST_UPDATE_DATE = GETDATE()
					WHERE
						STATE_SRC_ID = @STATEPROVINCEID

				END
				ELSE
				BEGIN
				
				---> If we found out the row existed but there was no Delta, then we incriment skip counter
				
					SET @ROWS_SKIP = @ROWS_SKIP + 1

				END

			END
			
			--Implement the Cursor again,
			--repeat until it has iterated over all rows of data
		
			FETCH NEXT FROM DB_CURSOR INTO @STATEPROVINCEID, @STATEPROVINCECODE, @STATEPROVINCENAME, @SALESTERRITORY

		END
		
		--Clean up cursos, reallocate memory back to system
		
		CLOSE DB_CURSOR
		DEALLOCATE DB_CURSOR

--Run insert to runs table for audit/control/checkpoint info, 
--and make sure run completed sucessfully and 
--we have checkpoint for next run

		INSERT INTO [dbo].[RUNS] (RUN_NAME, RUN_DT, SOURCE_COLUMNS, ROWS_INS, ROWS_DEL, ROWS_UPD, ROWS_SKIP) 
			VALUES ('STATE_D', @NEWCHECKPOINT, @SOURCE_COLUMNS, @ROWS_INS, @ROWS_DEL, @ROWS_UPD, @ROWS_SKIP)

	END

END
GO

--once your happy with the above
--you can commit the stored procedure to the demo DWH DB

