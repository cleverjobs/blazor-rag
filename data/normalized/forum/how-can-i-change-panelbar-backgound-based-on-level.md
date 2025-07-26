# how can I change Panelbar backgound based on level

## Question

**Geo** asked on 24 Jul 2024

I would like to change the Panelbar backgound based on the hierarchy level. I have 3 level nesting in the PanelBarItem collections. On each level I would like a different color/background color scheme. This is my PanelBarItem class public class PanelBarItem
{
public int Level { get; set; }
public string Text { get; set; }
public bool Disabled { get; set; }
public string Url { get; set; }
public object Icon { get; set; }
public List <PanelBarItem> Items { get; set; }
} and this is my PanelBar data private List <PanelBarItem> LoadFAQData()
{
List <PanelBarItem> items=new List <PanelBarItem> ()
{
new PanelBarItem()
{
Level=0,
Text="Provider Transactions",
Icon=SvgIcon.Accessibility,
Items=new List <PanelBarItem> ()
{
new PanelBarItem()
{
Level=1,
Text="Can I perform both DDE and HIPAA batch transactions?",
Icon=SvgIcon.QuestionCircle,
Items=new List <PanelBarItem> ()
{
new PanelBarItem()
{
Level=2,
Text="Basic registration gives you the ability to perform DDE Transactions. You must check the box labeled \"I would like to do HIPAA Transactions\" and complete all required fields for HIPAA Batch Transactions."
}
}
},
new PanelBarItem()
{
Level=1,
Text="Why can't I submit a claim to this website?",
Icon=SvgIcon.QuestionCircle,
Disabled=false,
Items=new List <PanelBarItem> ()
{
new PanelBarItem()
{
Level=2,
Text="Under HIPAA, health plans are permitted to choose the coordination of benefits (COB) model they wish to perform, either the Provider-to-payer or the payer-to-payer method. We have chosen to use the payer-to-payer method of COB. We have entered into trading partner agreements with the Medicare contractors. These agreements permit us to receive claims electronically directly from Medicare. If you submit a claim to Medicare for one of the Policyholder s listed on our eligibility file, you need do nothing more, Medicare will forward the claim to us for processing."
}
}
},
new PanelBarItem()
{
Level=1,
Text="Is pre-certification required?",
Icon=SvgIcon.QuestionCircle,
Disabled=false,
Items=new List <PanelBarItem> ()
{
new PanelBarItem()
{
Level=2,
Text="No. However, Medicare Select policies require prior approval for scheduled admissions to non-network hospitals. Please contact the claims customer service department at 1-877-825-9337 for further assistance. "
}
}
},
...
