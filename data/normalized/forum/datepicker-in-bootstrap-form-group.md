# DatePicker in Bootstrap form-group

## Question

**TomTom** asked on 05 Sep 2019

I'm trying to get a DatePicker to display correctly in a page that's using Bootstrap `form-group` and `form-control` tags, but I'm not having much success. The TelerikDateInput component exposes the Class property, but I don't think the DatePicker (or at least it doesn't seem to from my experimentation and from the documentation? I've tried various ways of doing this, e.g. <div class="form-group"> <label for="dueDate" class="control-label col-md-4">Expected Arrival Date: </label> <div class="col-md-8"> <TelerikDatePicker Class="form-control" Format="dd/MM/yyyy" @bind-Value="@State.BillOfLadingVM.DueDate" /> </div> <ValidationMessage For="@(()=> State.BillOfLadingVM.DueDate)" /> </div> But I always get something along the lines of the attached image. Is there any way to get this to work?

## Answer

**Marin Bratanov** answered on 05 Sep 2019

Hi Tom, Are you using the Bootstrap theme we provide? On the Class property - there is one, it is listed in the API reference. The thing is that you don't need the "form-control" class, as it adds padding and borders, and we already have a layout on our components, it needs to be present only for simple elements. We do have some overrides to take care of those issues, but that may still be a work in progress in certain places. That said, I am attaching here a few files from the default project that show how this works for me with the Bootstrap theme we provide, so you can compare against it and see what's the difference. Regards, Marin Bratanov

### Response

**Tom** answered on 05 Sep 2019

Hi Marin Thanks for the example, I'll have a look at that. Which version of Bootstrap is the Telerik theme targeting, is it 4.x? Cheers, Tom

### Response

**Marin Bratanov** answered on 06 Sep 2019

Hi Tom, I think 4.something was the last one tested, with the SASS themes we have. If more concrete numbers are required, I could check with our front end architect to see if this information is available. Regards, Marin Bratanov
