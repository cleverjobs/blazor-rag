# What is the best approach to load some large data in Telerik Grid without Virtual scrolling?

## Question

**Noa** asked on 29 Nov 2024

I have a Telerik Grid and it freezes when it has almost 3k rows. I have identified two reasons for that. One: I have put custom margin and padding on cell-level. Suggest me some efficient way to achieve this style without hitting the performance issues Second: I have a TelerikSplitButton in one of my columns which makes it more slower. But even removing above two things, plain TelerikGrid still takes about 2-3 seconds to load only 3k rows. I have pagination on my grid but pagination sizes cannot be very smaller. I need to show Datasets in thousands or more. Suggest me some best approaches to achieve this with custom design and template.

## Answer

**Hristian Stefanov** answered on 02 Dec 2024

Hi Noam, I recommend checking out our dedicated blog post on Telerik Blazor Data Grid Performance Optimization (Ultimate Checklist). We also got another article that describes the existing methods for enhancing performance, which can be adopted to streamline the component's operation speed: Slow Performance Article. Regards, Hristian Stefanov Progress Telerik

### Response

**Noam** commented on 03 Dec 2024

Hi Hristian, Thanks for responding. So basically at this moment, I have 5k rows and two columns with no event being called on grid and it takes almost 20 seconds to load. There are no excess parameters that I am passing and no customization is there. Just a simple grid with 5000 rows. Data gets available in 700ms and then it takes 20 seconds to render 5k rows. In your above article, there were some real performance gained result which says: for 500 rows, it took 823.8ms. Does it mean it will take 8.24 seconds for 5k rows on that same machine? Here is my code: <TelerikGrid Data="@_DATA" Pageable="false"> <GridColumns> <GridColumn Visible="true" Field="@nameof(PartnerDto.Name)" Title="Partner Name" Filterable="true" Editable="false" MinResizableWidth="170"> </GridColumn> <GridColumn Visible="true" Field="@nameof(PartnerDto.IsActive)" Title="Headquarter" Filterable="true" Editable="false" Sortable="false" MinResizableWidth="150" /> </GridColumns> </TelerikGrid>

### Response

**Hristian Stefanov** commented on 03 Dec 2024

Hi Noam, Given your scenario, where you are experiencing a 20-second load time for 5,000 rows, there are several factors and potential optimizations to consider: Rendering Time Expectation: The time it takes to render 5,000 rows is not necessarily a linear multiple of the time it takes to render 500 rows. The rendering time can increase disproportionately due to the larger number of DOM elements and potential browser limitations. Therefore, while it took 823.8ms for 500 rows in the example, it does not directly imply that 5,000 rows will take 8.24 seconds. The increase in rendering time can be influenced by the complexity of the grid, the browser's efficiency, and the hardware capabilities. Grid Optimization Highlights (from the blog post in my previous message): OnRead Event: Utilize the OnRead event to load data in chunks. This approach helps manage the data flow and reduces the load on client-side rendering by fetching data as needed. Reduce DOM Complexity: Even with two columns, rendering 5,000 rows results in a significant number of DOM elements. Consider reducing the number of visible rows at a time by implementing paging or virtualization, even though you mentioned not using pagination. This can help significantly by only rendering the rows that are currently visible. By addressing these factors, you can improve the rendering time for your grid. Kind Regards, Hristian
