# Saving and loading state of sub-grids?

## Question

**Rud** asked on 10 Nov 2021

We have successfully implemented saving the state of our custom component main grid with browser local storage, using this example. We have sub-grids in the main grid via the DetailTemplate section, for example: <TelerikGrid Data="@Data" @ref="@GridReference"> <DetailTemplate> @{
var ctx=context as ExpandoObject; <CustomSubgrid Context="@ctx" Property="Expanded" @ref="@SubGrid"> </CustomSubgrid>
} </DetailTemplate> Each page using the custom main grid has a unique state storage key - e.g.: StateStorageKey="ThisPage_MainDynamicGrid" Is it possible to do a similar saving and loading of the sub-grids states, if they are dynamically loaded via the DetailTemplate?

### Response

**Rudolf** commented on 10 Nov 2021

I may add that we would like to implement it as a one-button solution, so part of the current Save & Load State buttons for the main grid.

## Answer

**Marin Bratanov** answered on 11 Nov 2021

Hi Rudolf, You can hook to the OnStateChanged and OnStateInit events of all grids and use lambdas to build unique and logical identifiers for their state. For example, the child grid can use the primary key of the parent row as part of the storage key. With this, there is no need to have buttons at all. If you want to do this on button clicks, though, things can get complicated as you will need to manage references to the child grids dynamically, and that's a little tough in Blazor. Regards, Marin Bratanov

### Response

**Rudolf** commented on 12 Nov 2021

Thank you for the feedback. We have decided to do it with the events as mentioned for now, and remove the buttons. We'll revisit the buttons and references to the child grids etc. later.
