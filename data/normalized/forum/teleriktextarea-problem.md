# TelerikTextArea problem

## Question

**Kon** asked on 24 Sep 2021

Hi, what is the reason when TelerikTextArea with Autosize=true gets height 0px? I have component containing TelerikTextArea with autosize=true. Using this component directly in Page, TelerikTextArea appears OK (height in style gets correct px value) but using within another component it gets 0px. TelerikTextArea is disabled in this case but when enabled, the same issue (however, after any change/keypress, height gets correct). Best regards Konrad

## Answer

**Marin Bratanov** answered on 28 Sep 2021

Hello Konrad, The most likely reason is some CSS cascade that goes through the parent component in the app. By default, the textarea has a min-height CSS rule that should prevent that from happening, so something is probably overriding it. I am attaching here a screenshot that illustrates this, and a small sample that works fine on my end in a blank project, so you can compare against them to find the difference causing the issue. If you can reproduce it with just those two files in a blank solution, please attach it here so we can have a look. Regards, Marin Bratanov Progress Telerik
