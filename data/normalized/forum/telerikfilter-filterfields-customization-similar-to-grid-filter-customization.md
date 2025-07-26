# TelerikFilter FilterFields customization similar to Grid Filter customization

## Question

**Wil** asked on 14 Apr 2023

Is there any way to alter/customize the TelerikFilter FilterFields to be able to set a Visible attribute or add a filter template to add your own code to be filtered by? I have a grid that has a few dropdown list columns that need those values to be in the filter and I have some filterfields that i want to hide under certain conditions. From the documentation, I could not see a way that this is possible. With grid columns I am able to set them visible true/false as well as add a FilterTemplate. I just want to know if its possible on a FilterField of a TelerikFilter? I only seem to be able to set the attributes Name, Label, and Type. Thank you!

### Response

**Dimo** commented on 19 Apr 2023

Hi William, this will be possible when we implement templates for the Filter component. Please vote and follow the public request for status updates. In the meantime, a possible workaround is to use manually implemented UI instead of the Filter component (e.g. a Form). When the user is done, create a Filter descriptor programmatically and supply it to the Grid via its state.
