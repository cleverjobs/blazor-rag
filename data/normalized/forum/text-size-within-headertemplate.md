# Text size within HeaderTemplate

## Question

**Dea** asked on 12 Jan 2021

Hi. I have a TelerikTileLayout with 6 tiles. 5 of them use simple <TileLayoutItem HeaderText="..."> for the headings, but for one I need to use <HeaderTemplate>. The text I add in the <HeaderTemplate> is not rendered the same size as the text I specify with HeaderText. Presumably I need to either add a span with a particular class, or some other element? Anyone got this working?

## Answer

**Dean** answered on 12 Jan 2021

Issue can be seen on documentation: [https://docs.telerik.com/blazor-ui/components/tilelayout/overview](https://docs.telerik.com/blazor-ui/components/tilelayout/overview) - attached

### Response

**Marin Bratanov** answered on 12 Jan 2021

Hi Dean, You can always inspect the built-in rendering and copy it to your custom template. The template is supposed to give you some more customization options and so it does not need to render the same way as the built-in Text feature. For example: <TelerikTileLayout ColumnWidth="200px" RowHeight="150px" Width="700px" Columns="3" Resizable="true" Reorderable="true"> <TileLayoutItems> <TileLayoutItem HeaderText="Simple Header Text, no content"> </TileLayoutItem> <TileLayoutItem HeaderText="Simple Header Text, some content" ColSpan="2"> <Content> You can put components in the tiles too. </Content> </TileLayoutItem> <TileLayoutItem ColSpan="2"> <HeaderTemplate> <h5 class="k-card-title"> Template that copies the built-in header text appearance </h5> </HeaderTemplate> <Content> <p> As with other render fragments, you can put <strong> any </strong> content here </p> </Content> </TileLayoutItem> </TileLayoutItems> </TelerikTileLayout> Regards, Marin Bratanov

### Response

**Dean** answered on 12 Jan 2021

I can do this obviously but it doesn't seem very futureproof - do Telerik guarantee that all future versions will output the same HTML? Could I suggest a feature request that by default, text appears the same size whether specified via HeaderText or HeaderTemplate?

### Response

**Marin Bratanov** answered on 13 Jan 2021

Hi Dean, While there are no plans at the moment to change the rendering, I could not guarantee that at some point in the future design systems and approaches used in the world won't change and that won't prompt a change in our rendering. If you are looking for complete uniformity among all tiles you have two options: copy the Telerik HTML into your templates (perhaps take it out in a component) or always use the same header for all tiles - either the header text, or a custom template that you fully control Regards, Marin Bratanov
