# Blazor TelerikGrid Editor Template Copy

## Question

**EdEd** asked on 22 Jun 2021

I understand from here: [https://docs.telerik.com/blazor-ui/components/grid/templates/editor](https://docs.telerik.com/blazor-ui/components/grid/templates/editor) That the Editor Template gets a copy of the original model. However not all the values are getting copied correctly for my model object. I'm using a SmartEnum property, [https://github.com/ardalis/SmartEnum,](https://github.com/ardalis/SmartEnum,) and that property is not getting copied correctly, basically, it's empty. I'm wondering how this "copy" is being made, cloned?, so I can update either the model of my SmartEnum instance. Thanks, Ed

## Answer

**Nadezhda Tacheva** answered on 25 Jun 2021

Hi Ed, Yes, as you correctly stated, when editing the Grid creates a copy of your original object (and it has a different reference). This is valid in both cases - when the built-in editing is used and when you are using Editor Template. That copy is a cloned instance of the original item and we are using the following approach for cloning the item: public static object Clone ( this object original ) { var type=original.GetType(); if (type.IsValueType || original is string ||
(type.GetInterface( "IEnumerable" ) !=null && !(original is IDictionary<string, object>)))
{ return original;
} else if (type.IsArray)
{ return ((Array)original).Clone();
} else if (type.IsClass)
{ var clone=Activator.CreateInstance(type);

clone.ClonePropertiesFrom(original); return clone;
} return original;
} public static void ClonePropertiesFrom ( this object target, object item ) { var type=target.GetType(); if ((item is IDictionary<string, object> dynamicObject))
{ var cloneDynamicObject=(IDictionary<string, object>)target; foreach ( var keyValuePair in dynamicObject)
{
cloneDynamicObject[keyValuePair.Key]=keyValuePair.Value;
}
} else { foreach ( var originalProp in type.GetProperties(BindingFlags.Public | BindingFlags.NonPublic | BindingFlags.Instance))
{ // skip props with IgnoreDataMemberAttribute because of the ef core lazy loading if (originalProp.CanWrite && originalProp.CustomAttributes.All(a=> a.AttributeType !=typeof (IgnoreDataMemberAttribute)))
{
originalProp.SetValue(target, originalProp.GetValue(item)?.Clone());
}
}
}
} I hope you will find that useful as a starting point in order to set up your data. If any further questions appear, please do not hesitate to contact us. Regards, Nadezhda Tacheva

### Response

**Ed** commented on 25 Jun 2021

Okay thanks, this helps and I can work around this :)
