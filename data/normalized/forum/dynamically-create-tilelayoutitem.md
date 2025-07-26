# Dynamically create tileLayoutItem

## Question

**Pau** asked on 10 May 2021

Hi The idea we have is to have a list of tileLayoutitems. The user starts with an empty TileLayout and starts a wizard, the wizard lets the user choose from a list which tilelayoutitems he or she wants to see. We save this information in our database. So then, we need code to populate the tilelayout with the choosen tilelayout items. Qeustion is this possible to do and how? Eric

### Response

**Andy** commented on 15 May 2021

I am doing something similar. I have a set of Razor components that I define and store in my backend to dynamically build my home page. I used RenderFragments. I inherent off the TileLayoutState: public class myComponentlayout : TileLayoutItemState { public string HeaderText { get; set; }=""; public string Class { get; set; }=""; public RenderFragment renderFragment { get; set; } } Load my list of Widgets and build the RenderFraments into a new list: case ENUMValues.Widget.W_F2COL: { one=new myComponentlayout(); one.renderFragment=(builder)=> { builder.OpenComponent(0, new WidgetFeatured2Col().GetType()); builder.AddAttribute(1, "IdWidgets", Widget.IdWidgets); builder.CloseComponent(); }; } break; Build the TileLayout dynamically off the created list of RenderFragments: <TelerikTileLayout Columns="6" Width="100%" RowHeight="150px" Reorderable="true" @ref="TileLayoutInstance"> <TileLayoutItems> @foreach (var item in list) { <TileLayoutItem RowSpan="@item.RowSpan" ColSpan="@item.ColSpan" HeaderText="@item.HeaderText" Class="@item.Class"> <Content> @item.renderFragment </Content> </TileLayoutItem> } </TileLayoutItems> </TelerikTileLayout> I use the MediaQuery and the GetState/SetState in OnAfterRenderAsync() to modify the row/col based on screen size. Not sure how efficient it is but I have everything working except for changing the order on different screen sizes

## Answer

**Nadezhda Tacheva** answered on 12 May 2021

Hi Eric, We have an opened feature request in our public

### Response

**Nadezhda Tacheva** answered on 07 Jun 2021

Hi, I just wanted to let you know that we added a knowledge base article for adding and removing tiles. It is now live along with a sample project in our public blazor-ui repository - Add and Remove Tiles. The application demonstrates a simple customizable dashboard which uses TileLayout component and allows adding and removing tiles from a collection to display the desired set of data in the main section. Since at this stage a Visible parameter is not included in the TileLayout state, the component in the sample project uses a bool field Visible in the tiles model to handle the conditional rendering of the tiles depending on its value. With that being said, as the tiles collection reference changes in the process, the component state cannot maintain the data for the removed items and thus when they are re-added, they appear at the last position. Such a configuration along with maintaining the TileItems state will be possible once this feature request is live as we discussed earlier in this thread. Regards, Nadezhda Tacheva
