# Create a editable tooltip system

## Question

**Mar** asked on 26 Aug 2022

Hi, I would like to get some input on creating an editable tooltip system. Each input field should have a question mark icon on the right. That shows some text when you hoover over it. Text should be stored in a database and users should be able to edit the text directly on the form. For edit, I imagine this: Hoover over should show the help text but also a small pencil ikon if the have the right to edit the text. Edit should show a new popup. For identifying the field in the database I could maybe use classname.fieldname and get it using reflection. The text should be fetch and set on mouse over. Can I get the classname.fieldname from the binding to the input field? and then use it in the function to get the text for the tooltip? Link to tooltip documentation Let os brainstorm together 😊

## Answer

**Tsvetomir** answered on 30 Aug 2022

Hi, Martin, Thank you for sharing the scenario you are willing to achieve. Indeed, the main purpose of the Tooltip component is to enhance the existing browser's tooltip. Therefore, it picks up the info from the title or alt attribute of the HTML element and displays it. It also exposes the option to supply a custom template. Any functionality regarding editing should be considered external to the Tooltip implementation. Based on the provided information, I can suggest that you use the template functionality. It uses a RenderFragment internally, hence, you can throw virtually anything in the template and it will be visualized. We do have a comprehensive documentation article on the Tooltip's template. Regarding the database fetch before showing the tooltip, bear in mind if the user happens to be experiencing a large latency, they might need to wait for the request to finish before the tooltip is shown. If it is possible, I can recommend that you preload the data in the metadata for the HTML elements and use it in the template directly via the exposed context (second example in the article above). As per the editing, there is no limitation on how exactly the functionality should be achieved since it is external for the tooltip. You can handle it according to your preferences and business-specific requirements. Let me know if additional clarifications are needed. Regards, Tsvetomir
