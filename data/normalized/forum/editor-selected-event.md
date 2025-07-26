# Editor Selected Event

## Question

**Bas** asked on 14 Jun 2023

Hi, ist there any "Selected" Event for the Editor? I would like to enable/disable custom Tools, based on Selection, like you do with the add/remove hyperlink button. Thanks

## Answer

**Tsvetomir** answered on 19 Jun 2023

Hi Bastian, If the editor has custom tools, then, most probably their actions are wired via the OnClick event of the respective tool. Based on the click, you would know what has been last clicked (and perhaps, track any subsequent clicks). Within the handler, you could enable/disable buttons on the fly. The editor does not expose an event such as "SelectedChanged" because it cannot know what is inside the custom tools. Within the custom tool, there might be several buttons or a split button. In order for the component to raise any related event, it would have to know exactly is within the toolbar. Let me know if additional clarifications are needed. Kind regards, Tsvetomir
