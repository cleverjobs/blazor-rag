# Grid - forcing a full page reload?

## Question

**Lar** asked on 29 Nov 2022

For some reason when I click a Save button in a grid column, it's firing OnInitializedAsync after the page has already been loaded. I don't want values I initialize to be re-initialized when I click the Save button. How can I stop an interaction with the grid from firing OnInitializeAsync? The grid seems to be forcing a full page re-load instead of just re-drawing the grid.

### Response

**Larry** commented on 30 Nov 2022

I needed to change ButtonType="ButtonType.Submit" to ButtonType="ButtonType.Button"

## Answer

**Larry** answered on 30 Nov 2022

change ButtonType="ButtonType.Submit" to ButtonType="ButtonType.Button"
