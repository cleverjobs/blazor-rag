# GridToolBarTemplate 100% width?

## Question

**Jas** asked on 09 Mar 2023

Any reason why I can't get 100% width inside the GridToolBarTemplate? <GridToolBarTemplate> <div class="container-fluid"> <div class="row"> <div class="col-6"> My stuff on the left </div> <div class="col-6 text-end"> My stuff on the right </div> </div> </div> </GridToolBarTemplate>

## Answer

**Ivan** answered on 12 Mar 2023

Just add display: block to your container <div class="container-fluid d-block">
