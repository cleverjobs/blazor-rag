# Display Sort Icon for TelerikGrid on Initial Load

## Question

**Nat** asked on 04 Apr 2025

We are implementing the TelerikGrid for a Blazor application and they have asked that the sort icons be displayed by default on the component's initial load, not after the user clicks in the header row. It seems to work this way in all of the demo examples. Is there a way to toggle the display so that sort icons display automatically?

## Answer

**Anislav** answered on 04 Apr 2025

Hi Nate, By default, the Grid does not sort the provided data automatically, so no sorting indicator is displayed. To resolve this, I usually handle the OnStateInit event, allowing me to define an initial state for the Grid. In this event handler, I include a Sort Descriptor to sort the first column during initialization. For further information, refer to the official documentation: [https://www.telerik.com/blazor-ui/documentation/components/grid/state#onstateinit](https://www.telerik.com/blazor-ui/documentation/components/grid/state#onstateinit) Regards, Anislav Atanasov

### Response

**Nate** commented on 04 Apr 2025

Thanks for the quick reply Anislav, I fixed it per the following: OnStateInit="@((GridStateEventArgs<EventsDto> args)=> AddDefaultEventsSort(args))" and private void AddDefaultComplianceSort ( GridStateEventArgs<ComplianceEventsDto> args ) {
args.GridState.SortDescriptors.Add( new SortDescriptor()
{
Member=nameof (ComplianceEventsDto.TractorId),
SortDirection=ListSortDirection.Descending
});
} Got me where I needed to be.
