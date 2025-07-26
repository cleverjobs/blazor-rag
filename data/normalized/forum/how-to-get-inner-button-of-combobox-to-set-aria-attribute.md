# How to get inner button of combobox to set ARIA attribute?

## Question

**Ste** asked on 30 Jan 2024

Hi, since not all ARIA attributes are supported, I have to set some attributes manually. Setting aria-required (e.g. for textbox controls) by JavaScript is working: function activateRequired ( targetControlId ) { if (targetControlId) {
field=document. getElementById (targetControlId); if (field) {
field. setAttribute ( "aria-required", "true" );
}
}
} Now I have to set aria-hidden for the internal button of combobox. Is it possible to get this button to set the attribute? Regards, Stefan

### Response

**Hristian Stefanov** commented on 01 Feb 2024

Hi Stefan, I presume that the TextBox components and ComboBox you are utilizing are encapsulated within a Form. Concerning the "aria-required" attribute, I confirm that an enhancement request has already been submitted on our Public Feedback Portal: [Accessibility] Add the 'aria-required' attribute to the inputs inside Form. Upon completion of this item, the "aria-required" attribute will automatically be applied to inputs, including TelerikTextBox. You can vote and subscribe to it to receive email notifications for status updates. Regarding the "aria-hidden" attribute, could you provide additional details about your configuration and the tools reporting the absence of the "aria-hidden" attribute as a necessary element for ComboBox accessibility compliance? This information will enable me to offer more precise assistance and insights on this matter. I eagerly await your response. Kind Regards, Hristian

### Response

**Stefan** commented on 01 Feb 2024

Hi Hristian, thank you for your answer. Setting the "aria-required" seems to work by using the JavaScript method. But good to hear that is is planned to set this attribute automatically when using a control inside of a form item. Since I do not use forms for every scenario, it would be better to have access to ARIA attributes directly (e.g. like implementation for "aria-label"). But as I wrote before: I can handle this behaviour. ;) Currently it seems that the "aria-hidden" of the internal button of combobox control (input with role "button") is already set to "true". I have to discuss and check together with the person who is responsible for accessebilty tests. But I think it is not required to set this attribute manually. Regards, Stefan

### Response

**Hristian Stefanov** commented on 02 Feb 2024

Hi Stefan, Thank you for getting back to me and updating me on the situation. Take your time for the accessibility testing. If anything else pops up, I'm at your disposal to assist with more information. Kind Regards, Hristian
