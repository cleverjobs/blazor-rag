# Multiple Selection Mode - no need for CTRL+click

## Question

**Joe** asked on 20 Oct 2020

Hello, I was wondering if it is possible when Multiple Selection Mode is turned on that you don't have to press CTRL first to select multiple dates. So what I want is the functionality that you get when you press CTRL+click but I don't want to press and hold CTRL. Or is there a workaround to make this possible?

## Answer

**Marin Bratanov** answered on 20 Oct 2020

Hi Joeri, You can add a checkbox for selection - clicking that checkbox does not require the Ctrl or Shift keys to extend the selection. You can also handle the RowClick event to store the current selection, and then in the SelectedItemsChanged event, you can use that, in addition to the current item to update the SelectedItems as desired. You may also find useful this enhancement idea where clicking the rows won't invoke selection behavior, so you can more easily rely on the RowClick event: Select rows only with checkboxes (clicking the rows to not affect selection). If so, Vote for it to raise its priority, and click the Follow button to get email notifications for status updates. Regards, Marin Bratanov

### Response

**Joeri** answered on 20 Oct 2020

Hi Marin, Thank you for your quick response, but I was talking about the Calendar component, not the DataGrid one :)

### Response

**Marin Bratanov** answered on 20 Oct 2020

Hi Joeri, My apologies, I have no idea why I thought this is about the grid :) For selecting ranges in a calendar, we have the DateRangePicker component [https://demos.telerik.com/blazor-ui/daterangepicker/overview](https://demos.telerik.com/blazor-ui/daterangepicker/overview) You could also use the range selection mode of the calendar too (see the third one): [https://demos.telerik.com/blazor-ui/calendar/selection](https://demos.telerik.com/blazor-ui/calendar/selection) With the multiple selection mode, you can use the ValueChanged event and get the currently selected date, store that and the next time the user changes it, you can compare it to the old value, see if it is later (or satisfies any other business logic), and then populate the SelectedDates list so that it contains all dates between the start and end you want. You can find some examples of handling that event here so you can start adding logic there. Regards, Marin Bratanov

### Response

**Joeri** answered on 20 Oct 2020

Hi Marik, Alright, I will check out the provided options and links. Thanks for the quick responses and I will get back here if I need further assistance :) Joeri
