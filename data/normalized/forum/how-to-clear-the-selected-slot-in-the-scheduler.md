# How to clear the selected slot in the Scheduler

## Question

**Kyl** asked on 11 Mar 2025

I have a Scheduler on a dialog with a radio button group. Selecting radio button displays a number of appointments in the calendar and the Scheduler allows the user to click one to select it. When they select another radio button, I have it retrieving a new list of appointments and they're rendered properly but the same slot is still selected. If that slot isn't in the list, it selects a different (I think based on the previously selected appointment's index). How can I clear the selected appointment index completely?

## Answer

**Anislav** answered on 11 Mar 2025

Hi Kyle, I was able to reproduce your issue and reviewed the Telerik components code. It seems that the selected appointment index is retained by one of the underlying internal components. Unfortunately, I don’t see a built-in way to change this behavior. One possible workaround is to force a re-render of the component. This could be achieved by displaying a loading or skeleton component right after the radio button is clicked and before the new data is fetched and displayed. While this is somewhat of a hack, it may be OK in your case. Here’s an example: [https://blazorrepl.telerik.com/mzORvmEM01uXU4tG06](https://blazorrepl.telerik.com/mzORvmEM01uXU4tG06) Regards, Anislav Atanasov

### Response

**Kyle** commented on 12 Mar 2025

Hi Anislav, Thanks for reviewing. That workaround might work for us. The skeleton might be a bit jarring for the size of the component but I'll test with a loader and see if we like that better than leaving it with the default behaviour. And I'll log a feature request to see if the selected appointment can be cleared. -- Kyle
