# -*- coding: utf-8 -*-

from odoo import models, fields, api

class AddFields(models.Model):
	_inherit = "crossovered.budget.lines"

	imejercido = fields.Float(string="Importe Ejercido",compute="_valor")
	imcomprometido = fields.Float(string="Importe Comprometido",compute="_valorr")


	@api.one
	@api.depends('planned_amount','practical_amount')
	def _valor(self):
		self.imejercido = self.planned_amount - self.practical_amount
		
	@api.one
	@api.depends('general_budget_id','imcomprometido')
	def _valorr(self):
		comp=0
		for l in self.general_budget_id.account_ids:
			cr = self.env.cr
			sql = "select COALESCE(sum(ail.price_total),0) from account_invoice_line ail inner join account_invoice ai on ai.id=ail.invoice_id where ai.state='draft' and ai.type='out_invoice' and ail.account_id='"+str(l.id)+"'"
			cr.execute(sql)
			m = cr.fetchone()
			if m is None:
				m=(0,)
			comp = comp + max(m)
		self.imcomprometido = comp
