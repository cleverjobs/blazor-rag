# TabIndex on input components

## Question

**kha** asked on 13 Aug 2020

Hello, i tried to use TabIndex with components so when user hits tab it automatically changes the focus to next component but it doesn't work and i couldn't find a useful documentation

## Answer

**Svetoslav Dimitrov** answered on 13 Aug 2020

Hello Khashayar, While working on your ticket I have noticed that some of our input components lack the TabIndex property. I have opened a Feature Request for adding that property to all of them. You can see it from this link and I have given your Vote for it to raise the popularity of the item. You can Follow it for email notifications on status updates. That being said, below you can see the list of our components which currently support it: TelerikTextBox TelerikCheckBox TelerikDropDownList TelerikButton If you are using some of our other inputs that do not support it, I would suggest you wrap them around a div and provide the tabindex to that div as a workaround for the time of the implementation. Regards, Svetoslav Dimitrov
