from work.models import Ocp_Skill_Type, Ocp_Artwork_Type
from general.models import Artwork_Type, Job

def get_rt_from_ocp_rt(gen_rt):
    rt = None
    if hasattr(gen_rt, 'resource_type') and gen_rt.resource_type:
        rt = gen_rt.resource_type
    else:
        if isinstance(gen_rt, Artwork_Type):
            try:
                grt = Ocp_Artwork_Type.objects.get(id=gen_rt.id)
                rt = grt.resource_type
            except:
                rt = False
    return rt

def get_ocp_rt_from_rt(rt):
    gen_rt = None
    if hasattr(rt, 'ocp_resource_type') and rt.ocp_resource_type:
        gen_rt = rt.ocp_resource_type
    else:
        try:
            gen_rt = Ocp_Artwork_Type.objects.get(resource_type=rt)
        except:
            gen_rt = False
    return gen_rt


def get_rt_from_ocp_st(gen_st):
    rt = None
    if hasattr(gen_st, 'resource_type') and gen_st.resource_type:
        rt = gen_st.resource_type
    else:
        if isinstance(gen_st, Ocp_Skill_Type):
            try:
                gst = Ocp_Skill_Type.objects.get(id=gen_st.id)
                rt = gst.resource_type
            except:
                rt = False
    return rt

def get_ocp_st_from_rt(rt):
    gen_st = None
    if hasattr(rt, 'ocp_skill_type') and rt.ocp_skill_type:
        gen_st = rt.ocp_skill_type
    else:
        try:
            gen_st = Ocp_Skill_Type.objects.get(resource_type=rt)
        except:
            gen_st = False
    return gen_st

from django.conf import settings
if "pinax.notifications" in settings.INSTALLED_APPS:
    from pinax.notifications import models as notification
    from pinax.notifications.hooks import hookset
else:
    notification = None

def set_user_notification_by_type(user, notification_type="work_new_account", send=True):
    sett = None
    if notification:
        nott = notification.NoticeType.objects.get(label=notification_type)
        sett = user.noticesetting_set.filter(notice_type=nott)
        if not sett:
            for medium_id, medium_display in notification.NOTICE_MEDIA:
                if medium_display == 'email':
                    medium = medium_id, medium_display
                    sett = hookset.notice_setting_for_user(user, nott, medium_id)
        else:
            if not len(sett) == 1:
                raise ValidationError("(set_user_notification_by_type) The user has not exactly 1 notice setting for the notice type: "+str(notification_type)+" / User: "+str(user))
            sett = sett[0]
        sett.send = send
        sett.save()
    return sett




"""
def init_resource_types():
  news = ['news:']
  updt = ['updt:']
  errs = ['errs:']
  typ = Artwork_Type.objects.get(clas='Resource')
  artwks = Artwork_Type.objects.filter(lft__gte=typ.lft, rght__lte=typ.rght, tree_id=typ.tree_id)
  ocprts = Ocp_Artwork_Type.objects.all()
  if artwks.count() > ocprts.count():
    mtyp = Artwork_Type.objects.get(clas='Material')
    mts = Artwork_Type.objects.filter(lft__gte=mtyp.lft, rght__lte=mtyp.rght, tree_id=mtyp.tree_id)
    ocpmts = Ocp_Material_Type.objects.all()
    for ot in ocpmts:
      try:
        qst = Ocp_Artwork_Type.objects.filter(id=ot.id).update(
            artwork_type = ot.material_type,
            facet_value = ot.facet_value,
            resource_type = ot.resource_type
        )
        if qst.count():
          updt.append(qst.get().name)
        else:
          errs.append('?'+ot.name)
      except:
          aty = Artwork_Type.objects.get(id=ot.id)
        #try:
          #aty = Artwork_Type.objects.get(id=ot.id)
          qst = Ocp_Artwork_Type.objects.create(
            artwork_type = aty.typ_id,
            #artwork_type_ptr_id = aty.id,
            #typ_id = aty.typ_id,
            #name = aty.name,
            #description = aty.description,
            #clas = aty.clas,
            #facet_value = ot.facet_value,
            #resource_type = ot.resource_type
          )
          if qst.count():
            news.append('*'+qst.get().name)
          else:
            errs.append('Q:'+str(qst))
        #except:
        #  errs.append('a:'+aty.name)

    ocpnts = Ocp_Nonmaterial_Type.objects.all()
    for ot in ocpnts:
      try:
        qst = Ocp_Artwork_Type.objects.filter(id=ot.id).update(
            artwork_type = ot.material_type,
            facet_value = ot.facet_value,
            resource_type = ot.resource_type
        )
        if qst.count():
          updt.append(qst.get().name)
        else:
          errs.append('?'+ot.name)
      except:
        try:
          aty = Artwork_Type.objects.get(id=ot.id)
          qst = Ocp_Artwork_Type.objects.create(
            artwork_type = aty,
            facet_value = ot.facet_value,
            resource_type = ot.resource_type
          )
          if qst.count():
            news.append(qst.get().name)
          else:
            errs.append('A:'+aty.name)
        except:
          errs.append(ot.name)

    news.extend(updt)
    news.extend(errs)
    return ', '.join(news)
  else:
    return 'clean'


def update_from_general(clas=None):
  news = ['news:']
  updt = ['updt:']
  if clas == "Material_Type":
    try:
      gen_mts = Material_Type.objects.all() #filter(lft__gte=typ.lft, rght__lte=typ.rght, tree_id=typ.tree_id)
      ocp_mts = Ocp_Material_Type.objects.all() #filter(lft__gte=typ.lft, rght__lte=typ.rght, tree_id=typ.tree_id)
      for mt in gen_mts:
        if not mt in ocp_mts:
          obj = Ocp_Material_Type.objects.create( #mt )
            material_type = mt,
            #id=mt.id,
            name=mt.name,
            description=mt.description,
            parent=mt.parent
          ).get()
          news.append(obj)
          #break
        else:
          #pass
          obj = Ocp_Material_Type.objects.filter(id=mt.id).update( #mt )
            #id=mt.id,
            name=mt.name,
            description=mt.description,
           #lft=mt.lft,
           #rght=mt.rght,
           #tree_id=mt.tree_id,
            parent=mt.parent
          ).get()
          updt.append(obj) #.append(update)
      return news.append(updt)
    except:
      pass

  elif clas == "Nonmaterial_Type":
    try:
      gen_nts = Nonmaterial_Type.objects.all() #filter(lft__gte=typ.lft, rght__lte=typ.rght, tree_id=typ.tree_id)
      ocp_nts = Ocp_Nonmaterial_Type.objects.all() #filter(lft__gte=typ.lft, rght__lte=typ.rght, tree_id=typ.tree_id)
      for nt in gen_nts:
        if not nt in ocp_nts:
          obj = Ocp_Nonmaterial_Type.objects.create( #nt )
            nonmaterial_type = nt,
            #id=nt.id,
            name=nt.name,
            description=nt.description,
            parent=nt.parent
          ).get()
          news.append(obj)
          #break
        else:
          #pass
          obj = Ocp_Nonmaterial_Type.objects.filter(id=nt.id).update( #nt )
            #id=nt.id,
            name=nt.name,
            description=nt.description,
            parent=nt.parent
          ).get()
          updt.append(obj)
      return news.append(updt)
    except:
      return 'error'
  elif clas == "Skill_Type":
    #try:
      gen_sts = Job.objects.all() #filter(lft__gte=typ.lft, rght__lte=typ.rght, tree_id=typ.tree_id)
      ocp_sts = Ocp_Skill_Type.objects.all() #filter(lft__gte=typ.lft, rght__lte=typ.rght, tree_id=typ.tree_id)
      for st in gen_sts:
        if not st in ocp_sts:
          obj = Ocp_Skill_Type.objects.create(#st).get()
            #job_id=st.pk,
            id=st.id,
            name=st.name,
            description=st.description,
            parent=st.parent,
            verb=st.verb,
            gerund=st.gerund
          ).get()
          news.append(obj)
          #break
        else:
          #pass
          obj = Ocp_Skill_Type.objects.filter(id=st.id).update( #st )
            #id=st.id,
            name=st.name,
            description=st.description,
            parent=st.parent,
            verb=st.verb,
            gerund=st.gerund
          ).get()
          updt.append(obj)
      return news.append(updt)
    #except:
    #  return 'error'
  else:
    return clas
"""
