# Tooltip for text in TelerikEditor

## Question

**Luc** asked on 08 Dec 2022

Hello, I have to mark some text in the TelerikEditor and I'm using span for that: Anamnese <span class='code-marked' title='S52, S60, S63'> robert </span>, 14 år, V=50 I would like to have the "title" displayed as a tooltip but when I inspect the element in the TelerikEditor the "title" is removed. Is there a way to use css or something similar to add tooltip for words in TelerikEditor? Is there any way to keep the "title" ? TIA Lucian

## Answer

**Nadezhda Tacheva** answered on 13 Dec 2022

Hi Lucian, You are correct, the title attribute is indeed removed from the <span> tags. A colleague of yours has raised this question a while ago. In summary, the reason for this behavior is that our Editor engine defines tags and attributes that are explicitly allowed and everything else is stripped. For example, the title attribute is only allowed for <a> and <img> tags, because it is commonly used with them. Our suggestion to handle the scenario was to modify our JavaScript source code to add more permitted tags and attributes - you can find the source in the Downloads section of your account. The following folder contains the schema: /javascript/src/editor/config Were you able to try this approach and did you face some difficulties with that? In regards to a built-in functionality, this request was opened as a result of the discussion: Allow custom schema in the Editor We prioritize the requests based on the community demand (gathered votes). You may as well follow it to keep track of its progress. Regards, Nadezhda Tacheva Progress Telerik
