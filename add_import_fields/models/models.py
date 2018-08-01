# -*- coding: utf-8 -*-

from odoo import models, fields, api

class AddFields(models.Model):
	_inherit = "crossovered.budget.lines"

	imejercido = fields.Float(string="Importe Ejercido",compute="_valor")
	imcomprometido = fields.Float(string="Importe Comprometido",compute="_valorr")


	@api.one
	@api.depends('planned_amount','practical_amount')
	def _valor(self):
		if(self.practical_amount <= 0):
			self.imejercido = (self.planned_amount)+(self.practical_amount)
		else:
			self.imejercido = (self.planned_amount)-(self.practical_amount)
		
	@api.multi
	@api.depends('general_budget_id','imcomprometido')
	def _valorr(self):
		comp=0
		for l in self.general_budget_id.account_ids:
			cr = self.env.cr
			sql = "select COALESCE(sum(pol.price_total),0) from purchase_order_line pol inner join purchase_order po on po.id=pol.order_id where po.date_order>='"+str(self.date_from)+"' and po.date_order<='"+str(self.date_to)+"' and (po.state='draft' or po.state='sent' or po.state='to approve') and pol.account_analytic_id='"+str(l.id)+"'"
			cr.execute(sql)
			m = cr.fetchone()
			if m is None:
				m=(0,)
			comp = comp + max(m)
		self.imcomprometido = comp
