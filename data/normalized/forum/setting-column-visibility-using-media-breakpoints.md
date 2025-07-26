# Setting column visibility using media breakpoints

## Question

**Mic** asked on 26 Mar 2020

Can you provide an example of how to set column visibility using media breakpoints? For example, I want to be able to display more columns when the user is using an application from a desktop browser and just the essential columns when it's viewed on a phone.

## Answer

**Marin Bratanov** answered on 27 Mar 2020

Hello Michael, You can use an if-block in the markup to render the columns only when needed. We do something similar in this sample app: [https://github.com/telerik/blazor-stocks/blob/master/Client/Pages/RealTime.razor#L47.](https://github.com/telerik/blazor-stocks/blob/master/Client/Pages/RealTime.razor#L47.) In this sample we use a small package that offers some responsive design ( [https://github.com/EdCharbeneau/BlazorSize](https://github.com/EdCharbeneau/BlazorSize) ) - in this case we use the window.resize event to determine what to do, you can also tie the properties to media queries. Regards, Marin Bratanov

### Response

**Michael** answered on 27 Mar 2020

Thanks-- I'll check it out.

### Response

**Daniel** answered on 15 May 2020

Hello Marin, I tried BlazorSize on my grid and it works. However I noticed that grid columns that rely on the media queries always get added to the end of the grid. For example, if I have a grid with four columns, and I want to hide middle columns #2 and #3 on small screens, the grid will always display them in the order 1, 4, 2, 3. Is there any way around this without repeating the column definitions for each size scenario?

### Response

**Marin Bratanov** answered on 16 May 2020

Hi Daniel, The following feature needs to be implemented for this to happen: [https://feedback.telerik.com/blazor/1434835-preserve-column-order-when-showing-hiding-columns-dynamically.](https://feedback.telerik.com/blazor/1434835-preserve-column-order-when-showing-hiding-columns-dynamically.) In my last post there I have added a workaround through a loop over a column descriptor collection - if you populate the collection as desired, the order of the columns will come from the order of the models in the collection. Regards, Marin Bratanov

### Response

**Daniel** answered on 18 May 2020

Hi Marin, Thank you for the reply and the link. This approach works well as long as I don't specify any widths on the columns. The grid's underlying table has a colgroup element that retains the original column widths even after they are dynamically regenerated.

### Response

**Marin Bratanov** answered on 18 May 2020

Hi Daniel, You can track that here: [https://feedback.telerik.com/blazor/1466356-changing-the-grid-columns-collection-shows-the-new-columns-with-the-initial-widths.](https://feedback.telerik.com/blazor/1466356-changing-the-grid-columns-collection-shows-the-new-columns-with-the-initial-widths.) Regards, Marin Bratanov

### Response

**Jason** answered on 09 Sep 2020

I'm trying to do the same which is simple with Bootstrap. Is adding class to columns on the roadmap? I want to just add class=".d-none .d-xl-block"

### Response

**Marin Bratanov** answered on 10 Sep 2020

Hi Jason, We are considering an event that will let you do that: [https://feedback.telerik.com/blazor/1456957-conditional-row-and-cell-class-for-styling.](https://feedback.telerik.com/blazor/1456957-conditional-row-and-cell-class-for-styling.) If that would serve your needs, feel free to click the Vote button to raise its priority. If now, please add a comment on how you expect that to be exposed so we can take it into account when implementing that functionality. Regards, Marin Bratanov

### Response

**Jason** answered on 10 Sep 2020

If it includes the ability to add Class to the TH and TD then yes. This may also fix the spacing issues with Column widths if you allowed a class rather than Width in GridColumn. <th class="d-none d-xl-block"></th> <td class="d-none d-xl-block"></td>

### Response

**Curt** answered on 11 Feb 2021

Marin, I cannot get the example you mention in this thread to work at all. There seems to be multiple projects involved. I have implemented exactly as the instructions indicate but I get this error? Cannot provide a value for property 'listener' on type 'MyProject.Client.Pages.FetchData'. There is no registered service of type 'BlazorPro.BlazorSize.ResizeListener'. I copied his code exactly and it compiles and runs until I click on the FetchData link. I know this thread was written sometime ago, is there a more Telerik native solution yet? Any help you can provide is greatly appreciated! Curt

### Response

**Marin Bratanov** answered on 11 Feb 2021

Hi Curt, This looks like some missing setup for the BlazorSize package - maybe its service isn't registered when the application starts. I made an example here that shows how you can use it (basically, copied its readme) and then I added a grid where one of its columns is only visible on larger screens. It is attached to the end of this post. Regards, Marin Bratanov

### Response

**Curt** answered on 12 Feb 2021

Marin, Yes the project works exactly as I want mine to. It is probably because I am new to Blazor and have something set up incorrectly. Your sample project is different in that my project has the standard three WASM; Client, Server, and Shared. My project doesn't have a _host.chtml. It has an index.html in the wwwroot folder and I have made the reference to the package there.How should I configure this in the Client, then in the Server projects? Thank you again for the project. I know it will work I am just missing something. Curt

### Response

**Marin Bratanov** answered on 13 Feb 2021

Hi Curt, I simply used a server-side blazor project while you seem to be using a client-side blazor proeject, I can suggest you review resources like our online video training, or this free e-book on blazor, to get a better picture of the common things, and the differences between them. That said, I made an example for you that uses the same logic and package but on a WebAssembly project so you can compare them too. Regards, Marin Bratanov

### Response

**Ed** answered on 21 Jun 2021

Update: With the latest version of Telerik UI for Blazor you can use the new MediaQuery component as a replacement for BlazorSize. BlazorSize is still a valid solution, but the Telerik MediaQuery will reduce the number of dependencies in your project and is officially supported by Telerik. [https://docs.telerik.com/blazor-ui/components/mediaquery/overview](https://docs.telerik.com/blazor-ui/components/mediaquery/overview) Best regards, Ed Charbeneau Pr. Developer Advocate for Progress

### Response

**Unb** answered on 21 Jun 2021

@Ed this is very good news. I am trying to implement Telerik Blazor Chart to my project but I did not created my project as WebAssembly but server-client base so the sample was written for webassembly and it uses BlazorSize. The question is that how can I replace BlazorSize with MediaQuery? BlazorSize gives me the window size with a method called GetBrowserWindowSize. I checked the examples of MediaQuery in the telerik website. And pre-defined sizes have been used in the all examples. Such as <TelerikMediaQuery Media="(max-width: 600px)" OnChange="((changed)=> XSmall=changed)"></TelerikMediaQuery> OnChange method returns a boolean value and I created a ref object but could not find something related with size. As I understand, this component only gives us result whether it matches size of the media or not. here is the source code of the project which uses BlazorSide. Could you please check the client project? [https://github.com/telerik/blazor-ui/tree/master/sample-applications/blazor-stocks](https://github.com/telerik/blazor-ui/tree/master/sample-applications/blazor-stocks) thank you

### Response

**Hristian Stefanov** answered on 24 Jun 2021

Hi Unb, Indeed, TelerikMediaQuery component reports if the viewport size matches the condition in its Media attribute. The component does not have a method like GetBrowserWindowSize. Can you please share scenarios where such a method can be valuable and how it should be used? This feedback is helpful for us. We have a couple of examples with a responsive Chart and MediaQuery: [https://docs.telerik.com/blazor-ui/components/mediaquery/integration#chart-integration](https://docs.telerik.com/blazor-ui/components/mediaquery/integration#chart-integration) [https://github.com/telerik/blazor-ui/tree/master/chart/responsive-chart](https://github.com/telerik/blazor-ui/tree/master/chart/responsive-chart) Let me know if you need any additional information. Thank you. Regards, Hristian Stefanov
