import openerp
from openerp import netsvc, tools, pooler
from openerp.osv import fields, osv
from openerp.tools.translate import _
import time

class worksite(osv.osv):
  _name='worksite.worksite'
  
  _columns = {
      'active'  : fields.boolean('Active'),
      'name'    : fields.char('Name', size=128, required=True),
      'place'   : fields.char('Place', size=128, required=False),
      'type'    : fields.many2one('worksite.type', 'Type', required=True),
      'step'    : fields.many2one('worksite.step', 'Step', required=True),
      'workers' : fields.many2many('res.users', 'worksite_worker_rel', 'worksite_id', 'user_id', 'Worksite workers', help="Workers who are worjing on this worksite"),
      'stock_picking': fields.many2many('stock.picking', 'worksite_stock_picking_rel', 'worksite_id', 'stock_picking_id', 'Stock mouvments', help="Stock mouvments"),
  }
  
  _defaults = {
    
  }
  
  def set_nice_name(self, cr, uid, ids, context=None):
    """
      DEMO
      add "! name !" to name
    """
    
    name = '! '
    this = self.browse(cr, uid, ids, context=context)[0]
    name += this.name + ' !'
        
    self.write(cr, uid, ids, {'name': name })
    
    return True

worksite()
  
class WorksiteType(osv.osv):
  _name='worksite.type'
  
  _columns = {
      'name' : fields.char('Name', size=128, required=True)
  }
  
WorksiteType()
  
class WorksiteStep(osv.osv):
  _name='worksite.step'
  
  _columns = {
      'name' : fields.char('Name', size=128, required=True)
  }

WorksiteStep()