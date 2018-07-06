USE Your_Database

CREATE TABLE dbo.TestData
	(
	CustomerNumber INT,
	OrderNumber INT,
	Amount MONEY
	)

DECLARE @Count INT, @CustomerNumber INT, @OrderNumber INT, @Amount INT

SET @Count = 0

WHILE @Count < 4800001 
	BEGIN
		SET @CustomerNumber = FLOOR(RAND()*(3154368-1+1))+1;
		SET @OrderNumber = FLOOR(RAND()*(3154368-1+1))+1;
		SET @Amount = FLOOR(RAND()*(1000-1+1))+1;
		INSERT INTO dbo.TestData VALUES (@CustomerNumber,@OrderNumber,@Amount)
		SET @Count = @Count + 1
	END
