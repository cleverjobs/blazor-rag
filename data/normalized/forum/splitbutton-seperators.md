# SplitButton: Seperators ?

## Question

**Hen** asked on 02 Aug 2023

Is there any chance to use seperators within the menu ?

## Answer

**Dimo** answered on 04 Aug 2023

Currently that is possible only with CSS - <TelerikSplitButton> <SplitButtonContent> Reply </SplitButtonContent> <SplitButtonItems> <SplitButtonItem Class="separator-after"> Reply All </SplitButtonItem> <SplitButtonItem> Forward </SplitButtonItem> </SplitButtonItems> </TelerikSplitButton> <style>.separator-after { border-bottom: 1px solid red; padding-bottom: . 2em; margin-bottom: . 2em;
} </style>

### Response

**Hendrik** commented on 04 Aug 2023

Works perfectly ! Thank you so much ! Hendrik
