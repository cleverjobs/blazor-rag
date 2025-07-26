# Is there a ReadOnly toggle for Grid?

## Question

**Ser** asked on 13 Aug 2021

I know each column has an "Editable" property, but I was hoping there was something that could put the whole grid in read-only mode. Am I missing something, or is that simply not feasible? Thanks,

## Answer

**Marin Bratanov** answered on 13 Aug 2021

Hello Sergio, In a future version we will probably add a GridEditMode.None feature to the enum that currently holds the three available edit mode. SInce that might be a breaking change, it will have to wait for a major version release. You can Follow that here: [https://feedback.telerik.com/blazor/1529190-editmode-missing-none-option.](https://feedback.telerik.com/blazor/1529190-editmode-missing-none-option.) In the meantime, you can set EditMode to Inline and avoid adding any command buttons. Then you can also always cancel the OnEdit event. Regards, Marin Bratanov Progress Telerik

### Response

**Paul** commented on 27 Sep 2022

Hi is this added? Eric

### Response

**Hristian Stefanov** commented on 30 Sep 2022

Hi Eric, I confirm that the feature is available built-in. I have prepared an example for you to show a possible usage: REPL link.
