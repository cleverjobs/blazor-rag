# Add/Remove tile feature

## Question

**Joa** asked on 20 Apr 2021

Hello, we are trying to create a type of dashboard where the user would be able to customise the dashboard by removing and adding tiles. It seems like the add/remove feature is already implemented in Kendo UI for JQuery but not for Blazor, is there already an expected date for this feature to be implemented in Blazor?

## Answer

**Nadezhda Tacheva** answered on 23 Apr 2021

Hi Joao, We have an opened feature request in our public

### Response

**Nadezhda Tacheva** answered on 07 Jun 2021

Hi Joao, In the meantime, we added a knowledge base article for adding and removing tiles. It is now live along with a sample project in our public blazor-ui repository - Add and Remove Tiles. The application demonstrates a simple customizable dashboard which uses TileLayout component and allows adding and removing tiles from a collection to display the desired set of data in the main section. Since at this stage a Visible parameter is not included in the TileLayout state, the component in the sample project uses a bool field Visible in the tiles model to handle the conditional rendering of the tiles depending on its value. With that being said, as the tiles collection reference changes in the process, the component state cannot maintain the data for the removed items and thus when they are re-added, they appear at the last position. Such a configuration along with maintaining the TileItems state will be possible once this feature request is live as we discussed earlier in this thread. Regards, Nadezhda Tacheva Progress Telerik
