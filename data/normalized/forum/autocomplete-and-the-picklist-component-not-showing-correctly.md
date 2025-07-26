# Autocomplete and the Picklist component not showing correctly

## Question

**Ste** asked on 09 Apr 2021

Since the latest update (2.23) there seems to be in issue with the dropdown screen of the Autocomplete and the Picklist component. When they are displayed in a TelerikWindow, they become hidden behind the background of the window. See the attached screenshot for an example. (The box containing "test" is a a picklist, the autocomplete presents the same behavior)Is this an issue on my end or just a bug since the latest update?Thank you in advance.

## Answer

**Marin Bratanov** answered on 09 Apr 2021

Hi Stefan, Indeed, there is a regression issue caused by a new feature in the window. It will be fixed in our next release and here is a workaround: <style>.k-animation-container { z-index: 15000;
}
</style> Regards, Marin Bratanov Progress Telerik
