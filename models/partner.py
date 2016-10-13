# -*- coding: utf-8 -*-
from openerp import models, fields, api, _
from openerp.tools.translate import _


class ResPartner(models.Model):

	_inherit = "res.partner"

	def name_get(self, cr, uid, ids, context=None):
		if context is None:
			context = {}
		if isinstance(ids, (int, long)):
			ids = [ids]
		print "name_get for %s" % ids
		if context.get('name_without_company', False):
			print "name_without_company: %s" % ids
			res = []
			for record in self.browse(cr, uid, ids ,context=context):
				name = record.name or ''
				name = name.replace('\n\n','\n')
				res.append((record.id, name))
		else:
			res = super(ResPartner, self).name_get(cr, uid, ids, context=context)

		return res