# TelerikTileLayoutItem - How can I store my state in a db ? No ID of the tiles on the State?

## Question

**PAY** asked on 05 Oct 2021

Hi guys, My goal would be to store/retrieve my state from a database but I fail to understand how we can get the id of the reordered/resizeded tile? The TileLayoutState has no reference of the moving TileItem, the header text or any data really. It looks like it works with a defined set of TileItems but what if you don't know their numbers and positions or wish to change it? The SetState can't help with that because the initial State will not be the same. With my attached example, I have an initial Step1.png state, I change it to Step2.png. After my change one of the Test tiles is removed in the backend. How can I make sure next time I load the page I get Step2.png but without one of the Test tiles? Am I missing something or is it a limitation? Thank you for your help and keep up the good work on Blazor !

## Answer

**Marin Bratanov** answered on 06 Oct 2021

Hello, The tile order in the markup must match the order of their descriptors from the storage, you can read more about this here: [https://docs.telerik.com/blazor-ui/components/tilelayout/state.](https://docs.telerik.com/blazor-ui/components/tilelayout/state.) So, the goal is to initialize the tile layout wit the same tiles in the same order every time, and when the state is loaded their order will change visually without you having to do anything. At the moment, tiles do not carry unique identifiers. You can follow the implementation of such a Tag that they will carry here: [https://feedback.telerik.com/blazor/1489011-how-to-know-which-indiviadulal-tileitem-was-resized-tag-parameter-on-the-tile.](https://feedback.telerik.com/blazor/1489011-how-to-know-which-indiviadulal-tileitem-was-resized-tag-parameter-on-the-tile.) I see you've already added your Vote to it to raise its popularity too. Regards, Marin Bratanov

### Response

**PAYEN Christophe** commented on 06 Oct 2021

Hello Marin, Yes I figured it is probably the same issue with the Tag implementation after all. Will keep an eye on the thread and implement buttons to move the tiles myself in the meanwhile. Thank you for your answer.
