# New Card component: Resize, Reorder Events?

## Question

**Mar** asked on 12 May 2021

Hi: Does the new Card component raise events when the cards are resized or reordered? Do they support resize/reorder? Drag & Drop? I'm would like to determine if the Card component is a better choice than the TileLayout component as I will need to reorder, add, and delete cards/tiles based upon interaction with the user. Thanks marc

## Answer

**Marin Bratanov** answered on 12 May 2021

Hi Marc, The Card component is a display-only component - it just adds styling and exposes elements that let you do that styling through components rather than CSS. It is not and will not be resizable and reorderable, these are features for the full-blown TileLayout component and it already has them, together with Resize and Reorder events. You may also want to Follow this enhancement request so you can distinguish which particular tile the user moved/resized. For removing cards, Follow this - at the moment I imagine it will come through a Visible parameter on the tiles. I do believe you are aware of both of these feature requests, I am just confirming that they are the path forward for such functionality. Regards, Marin Bratanov

### Response

**Marc Simkin** commented on 12 May 2021

Hi Marin. Thank you. That is what I thought. Just wanted to confirm.
