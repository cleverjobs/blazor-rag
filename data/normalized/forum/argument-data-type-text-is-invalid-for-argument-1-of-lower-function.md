# Argument data type text is invalid for argument 1 of lower function.

## Question

**oni** asked on 06 Oct 2022

Is there any way to solve this problem if the data type is text in my DB? // Code result=await _db.Productos.Include(p=> p.CodigoEstadoNavigation) .Include(p=> p.IdCategoriaProductoNavigation) .ToDataSourceResultAsync(request);

### Response

**Marin Bratanov** commented on 08 Oct 2022

This sounds like a mismatch between what the grid thinks the field type is, and what it is in the database. Please make sure that they match (e.g., the grid model has an int where the column is int, not a string).
