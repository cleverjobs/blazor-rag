# Button in Header Template not firing OnClick unless button is clicked more than once

## Question

**BobBob** asked on 17 Feb 2022

I have a TileLayout with a TelerikButton in the HeaderTemplate and it does not fire unless I click on the button more that once. This seems to have started with v3 of the controls. <TileLayoutItem ColSpan="13" RowSpan="12" Class="scrollableTile"> <HeaderTemplate> <h5 class="k-card-title d-inline-block"> Hours </h5> <TelerikButton Class="float-end" Icon="save" Title="Save" OnClick="SaveHoursAsync"> </TelerikButton> </HeaderTemplate> <Content> </Content> </TileLayoutItem>

### Response

**Bob** commented on 17 Feb 2022

Yes. Thanks.

### Response

**Marin Bratanov** commented on 17 Feb 2022

I marked my post an answer for anyone hitting the same behavior to see easier. Sorry for orphaning your comment a little ^_^

## Answer

**Marin Bratanov** answered on 17 Feb 2022

Perhaps this is what you need: [https://feedback.telerik.com/blazor/1553733-prevent-tilelayout-from-stopping-the-click-event-in-the-tile-header?](https://feedback.telerik.com/blazor/1553733-prevent-tilelayout-from-stopping-the-click-event-in-the-tile-header?) If it is and this solves the issue, Vote and Follow it.
