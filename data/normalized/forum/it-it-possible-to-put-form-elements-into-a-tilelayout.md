# It it possible to put form elements into a TileLayout?

## Question

**Jst** asked on 11 Sep 2021

I would like to put individual form elements of a form into a tile layout so that the form elements can be moved around to suit the end user's layout preferences. Is it possible?

### Response

**Marin Bratanov** commented on 11 Sep 2021

You could try wrapping the entire TileLayout in a standard EditForm and see how that goes. The potential caveat here is that a change in the DOM may happen as tiles are reordered and if that breaks the validation (e.g., because Blazor loses some event handlers), you may need to re-create the validator in a suitable event such as the Reorder event of the tile layout (see an example of how to re-add a validator here ). NOTE: I am not sure that will happen, I have not tried the scenario, you should test it out.
