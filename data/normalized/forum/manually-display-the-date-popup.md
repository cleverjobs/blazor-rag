# manually display the date popup

## Question

**Dan** asked on 09 Apr 2022

Greetings, I want to make the DatePicker display by pressing F4 as other components do naturally, I already managed to make it display, but it only happens with the first DatePicker on the screen with the rest not working. each RadDatePicker, I assign a unique id, that's no problem could you explain to me how to make your control display the popup to select the date manually this is the structure of my HTML with its RadDatePicker <span class="k-datepicker wInput-date k-valid telerik-blazor k-input k-input-md k-input-solid k-rounded-md" data-id="cf018d18-c08c-477f-8a91-213944083232" data-val-id="938552dd-ed5a-4bea-833b-41f110a1c366" _bl_2d436386-enter code here7760-4ba0-9a8b-18c6033ed832=""> <span class="k-dateinput k-valid telerik-blazor k-input k-input-md k-input-solid k-rounded-md" role="combobox" aria-expanded="false" aria-haspopup="true"> <input class="k-input-inner" id="938552dd-ed5a-4bea-833b-41f110a1c366" tabindex="11" data-id="793b152c-d5e6-44b8-abef-fee3838ad1f5" type="text" _bl_cf0feb89-9608-41f7-a7d0-bcfab324c628=""> </span> <button class="telerik-blazor k-button k-input-button k-button-solid k-rounded-md k-button-rectangle k-button-md k-button-solid-base k-icon-button" id="8ec8f7d4-af4e-4340-9540-e424aa647b95" data-id="e0f6604d-8572-4aac-850d-d648a4c5ff37" tabindex="-1" aria-disabled="false" type="button"> <span class="k-icon k-i-calendar k-button-icon"> </span> </button> </span> So I managed to display the popup, of course the id I sent it from Blazor to JS $( "#938552dd-ed5a-4bea-833b-41f110a1c366" ). closest ( '.wInput-date' ). children ( "button" ). trigger ( "click" ); Use: Visual Studio 2022 Blazor Telerik 3.1 ASP Core 6

## Answer

**Svetoslav Dimitrov** answered on 13 Apr 2022

Hello Danny, Could you provide some more feedback on expanding the dropdown of components by pressing F4 as a built-in feature? I am asking because I am not aware of any browser/OS/Telerik component that provides such functionality out-of-the-box. On the topic of opening the dropdowns, we have an open feature request for a method exposed to the components reference. I have added your Vote for it, and you can click the Follow button to receive email notifications on status updates. Once this feature is implemented you can use a similar approach as in the Capture keyboard events in inputs knowledge-based article and use the open method. Now, I would like to touch upon the JS you have sent to us and the fact it works only for the first DatePicker on the page. From what I can see you are targeting the element by ID which would be unique to an instance of the component and thus only this instance would expand its dropdown. Regards, Svetoslav Dimitrov Progress Telerik

### Response

**Danny** answered on 13 Apr 2022

Greetings, thanks for responding in the RadDateTime of windows Forms that we use with yourselves, it has a natural way of displaying the date, pressing F4 when this component has the Focus, I think that they must maintain similarity in their components, that is, the same qualities that their components have in WinForms, and in Blazor. and even the same html input of type Date, has the quality that when pressing F4 the pop up of the date is displayed if I point to the id of the input, because when I put the id to the RadDetepicker it assigns it to the input it contains, which is very, that's why that is my guide, of course, each RadDatePicker that I generate has its own id, this is not repeated.

### Response

**Svetoslav Dimitrov** commented on 18 Apr 2022

Hello Danny, Indeed, this seems to be the default behavior of the dropdown in a desktop Windows application. To transfer the same behavior to a web suite you can use some JavaScript, as you have rightfully implemented until the open method is exposed for the component. In the web, the Id is a unique identifier of a single instance of an HTML element, or in this case - a Telerik UI for Blazor component. That is why, your code works only for the first (with this id) DatePicker, but not for the other. I would suggest you go with a Class (that is not a unique identifier), rather than Id.

### Response

**Danny** commented on 18 Apr 2022

hi svetoslav dimitrov It is not only the windows forms the date type input itself, it allows to display the date with F4 if the id is unique, in the example I point to a fixed id, but I receive that id as a parameter, expecting the id of the input where the F4 has been pressed, in order to get to the button next to the input.

### Response

**Svetoslav Dimitrov** commented on 21 Apr 2022

Hello Danny, I have spoken to our dev team about making the F4 key open the dropdown of the DateTimePicker (or any other component that has a dropdown) as a built-in feature. We have one major concern - most of the function keys have a reserved role across different browsers. As a component vendor, we should not interfere with the functions of the browser. That being said, I would say that making a custom JavaScript that opens the dropdown would be the best possible option. We have an open feature request for opening the dropdown on component focus (excuse me for not mentioning this sooner), and in the comment below, you can see a workaround until this feature is implemented. I would assume that a similar approach can be used to open the dropdown when the F4 key is pressed.
