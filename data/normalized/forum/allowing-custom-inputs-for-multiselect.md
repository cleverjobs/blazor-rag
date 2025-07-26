# Allowing custom inputs for MultiSelect

## Question

**Joh** asked on 05 Jan 2021

Hello, I have a MultiSelect component used to select tags. It works as intended, but I have one problem I can't find any workaround for : If the user inputs a text that isn't part of the data list, they can't "select" that value, unlike in a ComboBox for example where the data List "guides" you without restricting what you write. I have found no parameter that allows custom values, and I haven't been able to extract at all the raw text. To illustrate, here's a screenshot : I'd like to add / "select" a new value called "newTag" that is NOT part of the data list. When trying to retrieve the input value from the component (via 2-way binding or onChange event) , I only get a List<string> containing all selected/valid items, in this case a list with only "existing tag". I can't find a way whatsoever to retrieve that "newTag" text, it would probably solve the problem because then I could work around the lack of custom input permission in the OnChange event by adding dynamically "newTag" to the dataList, thus making it a valid value to select. Please help me find a way to implement custom inputs. Best regards

## Answer

**John** answered on 06 Jan 2021

It looks like the screenshot wasn't sent, let's try again :

### Response

**Nadezhda Tacheva** answered on 08 Jan 2021

Hi Johnny, I also consider the opportunity to add custom tags in the MultiSelect very useful feature. We currently have an open feature request for it in our public

### Response

**John** answered on 08 Jan 2021

Hi Nadezhda, Thanks for your answer. I'll check the sample project. I'm following the feature request in hope this will get implemented. Best regards, JF
