# TelerikGrid Error: Unexpected use of an unbound generic name

## Question

**Noa** asked on 24 Oct 2023

On all my <TelerikGrid> tags I am getting the error: Unexpected use of an unbound generic name on most of the values I pass into this grid except for FilterMode. The error does not prevent a build but I can't figure out how to get it to go away. The same thing is showing on all my grids and has always been there. Restarting visual studio does not fix it. See the code snippet below for the grid and my attachment shows a screenshot of the grid declaration code with the error lines. The [***] is just a stand in to anonymize the code. Can anyone explain what is causing the error? @using [***].Common.Dtos;
@using [***].Common.Enumerations;
@using [***].Features.EmployeeInfoAndTravelRequestLists.TravelRequestListingTab

@if (ViewModel is not null)
{ <!-- Render loader until grid initial data load is complete --> @if(!ShouldRenderGrid)
{
{ <div style="height:500px"> <TelerikLoaderContainer> </TelerikLoaderContainer> </div> }
} else
{ <TelerikGrid OnRead="@TravelRequestGridOnReadAsync" Class="grid-no-scroll" TItem="@TravelRequestFullDto" EnableLoaderContainer="true" Pageable="true" Sortable="true" SortMode="SortMode.Multiple" PageSize="10" SelectionMode="@GridSelectionMode.Single" FilterMode="GridFilterMode.FilterMenu"> <!-- dropdown, search box and new request button above grid --> <GridToolBarTemplate> <div class="dropdown-list-container"> <TelerikDropDownList Width="100px" Data="@ViewModel.EmployeeStatuses" @bind-Value="ViewModel.EmployeeStatusDDLSelectedValue"> <DropDownListSettings> <DropDownListPopupSettings Height="58px" /> </DropDownListSettings> </TelerikDropDownList> </div> <GridSearchBox Placeholder="Name/SAP/Personal ID..." Width="280px" /> <button class="new-request-button"> <span class="k-icon k-i-plus"> </span> New Request </button> </GridToolBarTemplate> <GridColumns> <GridCheckboxColumn SelectAll="false" Width="40px" /> <GridColumn Title="SAP Number" Width="195px"> <Template> @{
var SAPNumber=((TravelRequestFullDto)context).SAPNumber;
var RequestStatus=((TravelRequestFullDto)context).Status;
// render a chip in travel request number column if record has a request status <span> @SAPNumber <span class="cell-padding" /> <TelerikChip Class="travel-request-status-chip" Text=@TravelRequestStatusExtensions.ToDisplayValue(RequestStatus) Disabled=true Rounded="full" ThemeColor=@GetChipColorClass(RequestStatus) /> </span> } </Template> </GridColumn> <GridColumn Title="Workday Number" Field="@(nameof(TravelRequestFullDto.WorkdayNumber))" Width="140px" /> <!-- other grid columns here.... --> </GridColumns> </TelerikGrid> }
}

## Answer

**Noah** answered on 26 Oct 2023

I figured out the issue the TItem parameter of the TelerikGrid is expecting a type not a variable or value. So I just needed to take off the @and pass in TravelRequestFullDto instead of @TravelRequestFullDto.
