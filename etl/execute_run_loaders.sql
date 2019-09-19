use demoDB

DECLARE @return_value int

EXECUTE @return_value = [dbo].[RUN_LOADERS]

SELECT 'return_value' = @return_value

Go
---when monitoring run, observed large blockage at the disc level, professor notes this indicates it is running on workstation, 'even on servers, often find disc is your bottlneck on datawarehousing'
