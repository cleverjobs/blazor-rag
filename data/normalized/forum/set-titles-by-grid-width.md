# Set titles by grid width

## Question

**Pet** asked on 11 Nov 2020

Hi, how can I check the actual grid width to set abbreviated titles on small devices? Regards, Peter

## Answer

**Marin Bratanov** answered on 13 Nov 2020

Hello Peter, Once the user changes the state of the grid (say, resizes a column), the StateChanged event fires where all grid columns have widths. Before that, the standard HTML table rules apply, and they are described in detail in the Column Widths article. What is probably most relevant to your case is that if you have set widths to the columns, they will be respected. It is up to you to determine the actual px width if you use different units (such as em or rem). If you do not set widths to the columns it will be up to the browser to determine them and the grid does not know them either until a change occurs so it has to actually calculate them (see the first paragraph). With all that said, I think that you can use JS Interop to determine the viewport size and apply your desired business logic to the grid titles. Regards, Marin Bratanov
