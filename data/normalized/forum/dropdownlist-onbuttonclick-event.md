# DropDownList OnButtonClick Event

## Question

**Twa** asked on 14 Feb 2021

Hi. I want to populate a DropDownList (or a Combobox) everytime the associated button is pressed. I've tried with combobox "OnRead" event but it fires only the first time after the component is created. Any suggestion how to acchieve this? Thanks. Twain. PD: it's a shame that the components have so few events exposed. This implies constantly looking for hacks and workarounds to reach the expected result.

## Answer

**Marin Bratanov** answered on 15 Feb 2021

Hi Twain, The way to change the data a component shows depends on the framework - usually you simply need to provide a new collection reference. You can find some more guidance in the Refresh Data section of our docs. The dropdown could not possibly expose an event related to another button in the UI, if you want to change the data when some button is clicked, you must use the approach above. As for requesting data every time it opens - that is generally a bad practice for a generic component like ours because it would make the user interaction slow. If you have data that updates so often that you need to refresh it all the time, implementing a form of push notifications in the view-model is the better solution - this will let the data layer inform the UI there is new data when that happens so you can update it (e.g,.Add() or .Remove() from an observable collection ). Another approach that is commonly used for fetching data is cascading the dropdowns - so that the second requires a selection from the first before data is loaded and before it is enabled. This limits the amount of data you need to load, the frequency of those requests and states more clearly to the user what their flow in the application should be. You can find such examples in our demos and in this KB article. As for OnRead - the DropDownList does not have such an event because it does not have filtering yet. The ComboBox offers filtering and so you can customize what data it returns through OnRead. In our upcoming release the components will also have a Blur event where you could load data for next elements in the UI or, if you so choose, to update the data for the next run. Thus, I'd say the components expose the events they should, and changing the data in the view-model is not a hack, but the way the Blazor framework is designed. Regards, Marin Bratanov

### Response

**Twain** answered on 16 Feb 2021

Hi Marin. I understand your point and agree with you: requesting data every time the component opens is generally a bad solution but in some scenarios could be valid and efficient. If I have to populate a combo or dropdownlist with a list of files obtained from a directory in the local file system. As the content within the directory could change at any time then this modified "lazy loading" approach looks viable instead of polling the fs every x seconds and send a push to the UI. Thank for your response. Regards. Marcos.

### Response

**Marin Bratanov** answered on 17 Feb 2021

Hello Twain, I have extended this feature request with your case: [https://feedback.telerik.com/blazor/1506370-dropdown-container-popup-component-tied-to-an-anchor-for-positioning](https://feedback.telerik.com/blazor/1506370-dropdown-container-popup-component-tied-to-an-anchor-for-positioning) (the second paragraph in my edit on the opener post is to cover your case). I've added your Vote on your behalf to raise its priority too. Regards, Marin Bratanov

### Response

**Twain** answered on 17 Feb 2021

Marin, Thank you very much for your attention and the time dedicated to answering me . Regards. Twain.
