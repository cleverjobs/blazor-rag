# Appointment Editor Recurs Until Fields Disabled

## Question

**Joh** asked on 03 Jun 2020

Hey Blazor UI team, I've hit a block that I cannot get around with documentation on the scheduler component. Per the attached image, when I edit or create an appointment, the UI shows that the "End" field inputs are disabled. I found they are disabled with a particular css class, so it makes me think that I'm missing some sort of parameter or model field that the component is looking for. Is there documentation for this situation, and if not, what could be going on here? Thanks!

## Answer

**Marin Bratanov** answered on 04 Jun 2020

Hi John, Does our demo work fine for you, because it does for me (I am attaching a screenshot of what I see as a reference): [https://demos.telerik.com/blazor-ui/scheduler/recurring-appointments?](https://demos.telerik.com/blazor-ui/scheduler/recurring-appointments?) If the demo is OK, my best guess is that something is out of date on your machine - either the Telerik packages (we are at 2.14.1 at the moment, while looking at your account I see your license has expired around 2.9.0), or the Themes you are referencing are not the latest version (read more on how to reference them here ), or both. Regards, Marin Bratanov

### Response

**John** answered on 04 Jun 2020

Thanks for the response. I figured out what was going on. It's not clear that you must click the label of "After X Occurrences" or "On X date" to enable their inputs. It would be nice if those fields weren't disabled and if you click on the input box it would switch to that option, rather than forcing you to click on the label before the input is enabled. Another improvement would be hiding their input boxes unless they are selected. It would be useful to have the selected label be bolded as well.

### Response

**Marin Bratanov** answered on 05 Jun 2020

Hello John, I think the Themes in your project are either old, or customizations on them cause issues. I am attaching here a short video that shows how this should look like (from our demo) - the options that are not applicable are not visible so there isn't a way to make a mistake. Some options are shown as disabled (when not selected) so the user can see that they have those options. Regards, Marin Bratanov
