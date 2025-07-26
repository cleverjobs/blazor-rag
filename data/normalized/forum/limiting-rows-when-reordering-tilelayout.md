# Limiting # Rows When Reordering TileLayout

## Question

**Zac** asked on 30 Apr 2024

I have a layout of three tiles like so: <TelerikTileLayout Columns="3" RowHeight="18vh" Resizable="true" Reorderable="true"> <TileLayoutItems> <TileLayoutItem RowSpan="2" ColSpan="2"> <Content> content </Content> </TileLayoutItem> <TileLayoutItem RowSpan="4"> <Content> content </Content> </TileLayoutItem> <TileLayoutItem RowSpan="2" ColSpan="2"> <Content> content </Content> </TileLayoutItem> </TileLayoutItems> </TelerikTileLayout> I would like the tile layout to stay 4 rows in height, however when a user reorders one of the tiles in a certain way, it extends it down to a 5th row, and displaces one of the tiles in an unpleasing way, which I've shown in the attached image. I want to restrict the tile layout so that it stays 4 rows deep, but still allow my users to rearrange the tiles within that restricted space. Is this possible?

### Response

**Hristian Stefanov** commented on 02 May 2024

Hi Zachary, A feature request for TileLayout Constrain RowSpan and ColSpan has already been submitted on our public

### Response

**Zachary** commented on 02 May 2024

I dont think this would help, as I am looking to constrain the overall RowSpan of the entire TileLayout so that I may stop the user from making unintended layouts. The issue I am running into is that one of the tiles is creating a new row and then filling that space like shown in the attached image. This will happen even if the TileLayout has a fixed height. The RowSpan of the individual tiles is not changing when this happens, so constraining them would not solve the issue. Ideally, I'd like if the TileLayout component had a Rows parameter I could set to restrict automatically creating rows. I don't know enough about css grid styling to know how to achieve this. Is there a styling parameter I can overwrite to do this?

### Response

**Hristian Stefanov** commented on 07 May 2024

Hi Zachary, Thank you for getting back to me with feedback. I will discuss the scenario with our development team and get back to you very shortly with more details. Your patience is highly appreciated. Kind Regards, Hristian

### Response

**Hristian Stefanov** commented on 10 May 2024

Hi Zachary, I am ready to share an update from reviewing the case with the team. I confirm that the issue you encountered is indeed a bug in the TileLayout. I have created a public item on your behalf to address this: Reordering Tiles breaks the layout. You are automatically subscribed as a creator, which means you will receive email notifications regarding the status updates of this item. I am sorry for any inconvenience the issue may have caused you. Additionally, as a token of appreciation, I have credited your account with Telerik points for reporting the behavior. Kind Regards, Hristian
