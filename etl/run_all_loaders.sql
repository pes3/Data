--- let's create a stored procedure that will execute the loaders to make sure they execute in the order we need them to
use demoDB
go
CREATE OR ALTER PROCEDURE RUN_LOADERS AS 
BEGIN

DECLARE @RC INT

EXECUTE @RC = [dbo].[LOADER_STATE_d]
EXECUTE @RC = [dbo].[LOADER_CITY_D] 
EXECUTE @RC = [dbo].[LOADER_BUYING_GROUP_D]
EXECUTE @RC = [dbo].[LOADER_CUSTOMER_CATEGORY_d]
EXECUTE @RC = [dbo].[LOADER_DELIVERY_METHOD_D]
EXECUTE @RC = [dbo].[LOADER_PERSON_D]	
EXECUTE @RC = [dbo].[LOADER_CUSTOMER_D]		
EXECUTE @RC = [dbo].[LOADER_ORDER_F]		

END
GO