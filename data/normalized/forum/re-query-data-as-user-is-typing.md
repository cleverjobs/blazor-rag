# Re-Query Data as User is Typing

## Question

**Joh** asked on 05 May 2020

Is the autocomplete control the best way to handle a dynamic search using an external data source? Meaning the user might type "den" and the control would use an external data source to query an api or database, returning choices in the dropdown of "dennis" and "denise" and "deno" etc. I don't see any example of dynamic real time data source updates as the user is typing and interacting with the control. Am I missing something? Thank you for your guidance.

## Answer

**Marin Bratanov** answered on 05 May 2020

Hi John, You can use the OnRead event to get the user input ("den" in this example), and query the desired service in order to provide the appropriate data to the autocomplete. Here's an example: [https://docs.telerik.com/blazor-ui/components/autocomplete/events#onread](https://docs.telerik.com/blazor-ui/components/autocomplete/events#onread) Regards, Marin Bratanov

### Response

**Erna** answered on 16 Mar 2021

Hi Martin, i use this "OnRead=@ReadItems" to handle the dynamic external datasource for the AutoComplete but anyway the method "protected async Task ReadItems(AutoCompleteReadEventArgs args)" can only used when Filterable="true". My Problem is, i don't want to focus on the dropdown list element, i just want the cursor focused on the text what i'm typing, this can be done when Filterable not be set. How can i solve that problem? Thank you for your advice.

### Response

**Marin Bratanov** answered on 16 Mar 2021

Hello Erna, The OnRead event on the AutoComplete fires as the user types. Since the autocomplete is a free text input (meaning, the user is not obliged to choose on the of the suggestions you offer in its Data), it is, effectively, always filterable. If you want to provide a different list of suggestions based on the input, that's the Filterable functionality that you can extend through OnRead. The focus remains in the component while the user is typing regardless of the data you get in OnRead, however. If the user presses the Down arrow to go into the suggestions, they are no longer typing and it is expected that the focus will no longer be in the input. The dropdownlist element I am not sure I follow the problem - when the user types, the focus remains in the input, whether filtering is enabled or not. I'm attaching here a short video that shows what to expect from OnRead as a reference so you can see if you get different behavior. Regards, Marin Bratanov Progress Telerik

### Response

**Erna** answered on 17 Mar 2021

I take this autocomplete for searching, as developer i give my client suggestion what i have in database and renew it every time the client text it (with OnRead but i obliged to set Filterable="true"), but the client can surely search for something else. The Problem is: when the client click on the Enter-Button, the first suggestion will replace the search text what the client typed before. He don't want the suggestion text, he will just take the text he typed before. I can take "ValueChanged" without setting Filterable="true" and the client can searching what he want, but the suggestion ist one character too late. Do you have any advice?

### Response

**Marin Bratanov** answered on 17 Mar 2021

Hi Erna, To cancel the dropdown with suggestions the user can press Esc, and the currently "active" suggestion that will be selected has a highlight indicator - there is a border on it. The purpose of the autocomplete is to facilitate a choice from the predefined set of options. Enter is a confirmation of that choice. This is the core concept of that component and it cannot be avoided in its current implementation. How would you expect that to be provided while keeping the component functionality in place - since those are two contradicting behaviors? I am also attaching a short video to the end of this post that illustrates the expected behavior. Regards, Marin Bratanov
