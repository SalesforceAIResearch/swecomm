
# aider chat started at 2024-07-20 13:46:13

> Aider v0.37.1-dev  
> Models: gpt-4o with diff edit format, weak model gpt-3.5-turbo  
> Git repo: ../../../../private/var/folders/7q/_fx2smvd0hq3nkt98d3kt4f00000gn/T/tmp59a70pbn/.git with 6,655 files  
> Warning: For large repos, consider using an .aiderignore file to ignore irrelevant files/dirs.  
> Repo-map: using 2048 tokens  

#### ModelForm fields with callable defaults don't correctly propagate default values  
#### Description  
#### 	  
#### When creating an object via the admin, if an inline contains an ArrayField in error, the validation will be bypassed (and the inline dismissed) if we submit the form a second time (without modification).  
#### go to /admin/my_app/thing/add/  
#### type anything in plop  
#### submit -> it shows an error on the inline  
#### submit again -> no errors, plop become unfilled  
#### # models.py  
#### class Thing(models.Model):  
#### 	pass  
#### class RelatedModel(models.Model):  
#### 	thing = models.ForeignKey(Thing, on_delete=models.CASCADE)  
#### 	plop = ArrayField(  
#### 		models.CharField(max_length=42),  
#### 		default=list,  
#### 	)  
#### # admin.py  
#### class RelatedModelForm(forms.ModelForm):  
#### 	def clean(self):  
#### 		raise ValidationError("whatever")  
#### class RelatedModelInline(admin.TabularInline):  
#### 	form = RelatedModelForm  
#### 	model = RelatedModel  
#### 	extra = 1  
#### @admin.register(Thing)  
#### class ThingAdmin(admin.ModelAdmin):  
#### 	inlines = [  
#### 		RelatedModelInline  
#### 	]  
#### It seems related to the hidden input containing the initial value:  
#### <input type="hidden" name="initial-relatedmodel_set-0-plop" value="test" id="initial-relatedmodel_set-0-id_relatedmodel_set-0-plop">  
#### I can fix the issue locally by forcing show_hidden_initial=False on the field (in the form init)  
> 33884 prompt tokens, 111 completion tokens, $0.171085 cost  

To address the issue with callable defaults in `ModelForm` fields and the validation bypass in the admin inline, we will likely need to make changes to the following files:

1. `admin.py` - To modify the `RelatedModelForm` initialization to force `show_hidden_initial=False` on the field.
2. `models.py` - To ensure the model definitions are correct and potentially add any necessary adjustments.

Please add the following files to the chat so I can provide the necessary changes:

1. `admin.py`
2. `models.py`
