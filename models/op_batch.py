# -*- coding: utf-8 -*-

from odoo import api, fields, models


class OpBatch(models.Model):
    _inherit = 'op.batch'

    is_imported_record = fields.Boolean(default=False, string='¿Es registro importado de Odoo 12?')
    coordinator = fields.Many2one(comodel_name='res.partner', string='Coordinador')  # FIXME: DID I ASK ABOUT THIS FIELD ?
    campus_id = fields.Many2one(comodel_name='op.campus', string='Sede')  # OK - CREAR MODELO
    uvic_program = fields.Boolean(string='Programa UVIC', default=False)  # OK
    modality_id = fields.Many2one(comodel_name='op.modality', string='Modalidad')  # OK - CREAR MODELO
    students_limit = fields.Integer(string='Límite matrículas')  # OK FIXME: THIS FIELD HAS VALUE OF metadata_server_isep = MetaData(bind=server_isep) ???
    sepyc_program = fields.Boolean(string='Programa Sepyc / Sep', default=False)  # OK

    # INFORMACIÓN ACADÉMICA --------------------------------------------------------
    expiration_days = fields.Integer(string='Días de expiración', default=0)  # OK
    date_diplomas = fields.Datetime(string='Fecha de diplomas')  # OK
    academic_year = fields.Char(string='Año académico', size=16)  # OK
    generation = fields.Char(string='Generación', size=100)  # OK
    # --------------------------------------------------------------------------------------

    # SL ------------------------------------------------------------------------------
    # hours = fields.Float(string='Horas', compute='_calculate_hours')  # OK
    hours = fields.Float(string='Horas')  # OK
    # credits = fields.Float(string='Créditos', compute='_calculate_credits')  # OK
    credits = fields.Float(string='Créditos')  # OK
    # ects = fields.Float(string='ECTS', default=0, compute='_calculate_ects')  # OK
    ects = fields.Float(string='ECTS', default=0)  # OK

    # @api.one
    # @api.depends('op_batch_subject_rel_ids.hours')
    # def _calculate_hours(self):
    #     """
    #     Realiza la suma total de los horas colocadas en la relacion grupo asignaturas
    #     """
    #     self.hours = sum(subject_rel.hours
    #                      for subject_rel in self.op_batch_subject_rel_ids)

    # @api.one
    # @api.depends('op_batch_subject_rel_ids.credits')
    # def _calculate_credits(self):
    #     """
    #     Realiza la suma total de los creditos colocados en la relacion grupo asignaturas
    #     """
    #     self.credits = sum(subject_rel.credits
    #                        for subject_rel in self.op_batch_subject_rel_ids)

    # @api.one
    # @api.depends('op_batch_subject_rel_ids.ects')
    # def _calculate_ects(self):
    #     """
    #     Realiza la suma total de los ects en la relacion de grupo asignaturas
    #     """
    #     self.ects = sum(subject_rel.ects
    #                     for subject_rel in self.op_batch_subject_rel_ids)
    # ----------------------------------------------------------------------------------

    # RECONOCIMIENTOS - FIXME: REVISE WHAT IS THE RELATION THAT HAS THESE FIELDS WITH MODEL OP.COURSE
    acknowledgments = fields.Text(string='Reconocimientos', size=700)  # OK
    reconeixements = fields.Text(string='Reconoixements', size=700)  # OK

    # LATAM ----------------------------------------------------------------------------------------
    # practical_hours_total = fields.Float(string='Total de horas prácticas', compute='_compute_hours_course', store=True)  # OK
    practical_hours_total = fields.Float(string='Total de horas prácticas')  # OK
    # independent_hours_total = fields.Float(string='Total de horas independientes', compute='_compute_hours_course', store=True)  # OK
    independent_hours_total = fields.Float(string='Total de horas independientes')  # OK
    # theoretical_hours_total = fields.Float(string='Total de horas teóricas', compute='_compute_hours_course', store=True)  # OK
    theoretical_hours_total = fields.Float(string='Total de horas teóricas')  # OK

    # @api.one
    # @api.depends('op_batch_subject_rel_ids.subject_id.practical_hours',
    #              'op_batch_subject_rel_ids.subject_id.independent_hours',
    #              'op_batch_subject_rel_ids.subject_id.theoretical_hours')
    # def _compute_hours_course(self):
    #     self.practical_hours_total = sum(subject.subject_id.practical_hours
    #                                      for subject in self.op_batch_subject_rel_ids)
    #     self.independent_hours_total = sum(subject.subject_id.independent_hours
    #                                        for subject in self.op_batch_subject_rel_ids)
    #     self.theoretical_hours_total = sum(subject.subject_id.theoretical_hours
    #                                        for subject in self.op_batch_subject_rel_ids)

    # hours_total = fields.Float(string='Total de horas', compute='_compute_hours_total_course', store=True)  # OK
    hours_total = fields.Float(string='Total de horas')  # OK

    # @api.one
    # @api.depends('practical_hours_total', 'independent_hours_total', 'theoretical_hours_total')
    # def _compute_hours_total_course(self):
    #     self.hours_total = self.theoretical_hours_total + self.independent_hours_total + self.practical_hours_total

    # practical_hours_credits = fields.Float(string='Créditos horas prácticas', compute='_compute_credits_by_hours', store=True)  # OK
    practical_hours_credits = fields.Float(string='Créditos horas prácticas')  # OK
    # independent_hours_credits = fields.Float(string='Créditos horas independientes', compute='_compute_credits_by_hours', store=True)  # OK
    independent_hours_credits = fields.Float(string='Créditos horas independientes')  # OK
    # theoretical_hours_credits = fields.Float(string='Créditos horas teóricas', compute='_compute_credits_by_hours', store=True)  # OK
    theoretical_hours_credits = fields.Float(string='Créditos horas teóricas')  # OK

    # @api.one
    # @api.depends('practical_hours_total', 'independent_hours_total', 'theoretical_hours_total')
    # def _compute_credits_by_hours(self):
    #     """
    #     Calcula la cantidad de creditas por horas
    #     """
    #     min_hours_study_by_credit = 16
    #     self.practical_hours_credits = self.practical_hours_total / min_hours_study_by_credit
    #     self.independent_hours_credits = self.independent_hours_total / min_hours_study_by_credit
    #     self.theoretical_hours_credits = self.theoretical_hours_total / min_hours_study_by_credit

    # credits_total = fields.Float(string='Total de créditos', compute='_compute_credits_total_course', store=True)  # OK
    credits_total = fields.Float(string='Total de créditos')  # OK

    # @api.one
    # @api.depends('theoretical_hours_credits', 'independent_hours_credits', 'practical_hours_credits')
    # def _compute_credits_total_course(self):
    #     """
    #     Calcula la suma total de los creditos
    #     """
    #     self.credits_total = self.theoretical_hours_credits + self.independent_hours_credits + self.practical_hours_credits
    # ------------------------------------------------------------------------------------------------------

    # OTRA INFORMACIÓN --------------------------------------------------------------------------
    days_week = fields.Char(string='Días de la semana', size=50)  # OK
    schedule = fields.Char(string='Horario', size=200)  # OK
    contact_class = fields.Char(string='Contacto', size=200)  # OK
    type_practices = fields.Many2one(comodel_name='op.practices.type', string='Tipo de prácticas')  # CREAR MODELO - HERE ARE NOT RECORDS
