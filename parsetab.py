
# parsetab.py
# This file is automatically generated. Do not edit.
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftADDSUBTRACTleftASTERISKDIVIDEDIVIDE_INTINSERT INTO VALUES SET SELECT DELETE INT_LIT DOUBLE_LIT STRING_LIT ADD SUBTRACT DIVIDE DIVIDE_INT MODULO EQUAL EQUAL_NULL GT GE LT LE NE NOT COLUMN_NAME TABLE_NAME ASTERISK COMMA SEMICOLON OPENPAR CLOSEPAR FROM WHERE LIKE STRCMP IS NULL BETWEEN ANDstatement : insert_statement\n            | select_statement\n            | delete_statementinsert_statement : INSERT into_kw TABLE_NAME VALUES OPENPAR value_list CLOSEPAR SEMICOLON\n            | INSERT into_kw TABLE_NAME OPENPAR column_name CLOSEPAR VALUES OPENPAR value_list CLOSEPAR SEMICOLON\n            | INSERT into_kw TABLE_NAME SET assignment_list SEMICOLONselect_statement : SELECT columns FROM TABLE_NAME SEMICOLON\n            | SELECT columns FROM TABLE_NAME WHERE condition SEMICOLONdelete_statement : DELETE FROM TABLE_NAME SEMICOLON\n            | DELETE FROM TABLE_NAME WHERE condition SEMICOLONinto_kw : INTO\n            | emptycolumns : ASTERISK\n            | column_namecolumn_name : COLUMN_NAME\n            | column_name COMMA COLUMN_NAMEassignment_list : COLUMN_NAME EQUAL literals\n            | assignment_list COMMA COLUMN_NAME EQUAL literalsvalue_list : literals\n            | value_list COMMA literalsliterals : STRING_LIT\n            | INT_LIT\n            | DOUBLE_LITcondition : string_cond\n            | num_cond\n            | NOT OPENPAR string_cond CLOSEPAR\n            | NOT OPENPAR num_cond CLOSEPARstring_cond : string_exp LIKE string_exp\n            | string_exp NOT LIKE string_exp\n            | STRCMP OPENPAR string_exp COMMA string_exp CLOSEPARstring_exp : STRING_LITnum_cond : num_exp comparison_op num_exp\n            | num_exp BETWEEN num_exp AND num_exp\n            | num_exp NOT NULL\n            | num_exp IS NULLnum_exp : num_exp ADD num_factor\n            |  num_factor SUBTRACT num_exp\n            | num_factornum_factor : num_factor ASTERISK num_term\n            | num_factor DIVIDE num_term\n            | num_factor DIVIDE_INT num_term\n            | num_factor MODULO num_term\n            | num_termnum_term : OPENPAR num_exp CLOSEPAR\n            | num_valnum_val : INT_LIT\n            | DOUBLE_LIT\n            | COLUMN_NAMEcomparison_op : GE\n            | GT\n            | LE\n            | LT\n            | NE\n            | EQUAL\n            | EQUAL_NULLempty : '
    
_lr_action_items = {'STRCMP':([24,47,76,],[31,31,31,]),'INT_LIT':([24,28,34,47,56,59,60,61,62,63,64,65,67,68,69,70,72,73,74,75,76,82,103,106,108,],[41,49,41,41,49,41,41,41,41,41,-49,-54,-55,-51,-50,41,41,41,-53,-52,41,49,49,49,41,]),'INSERT':([0,],[2,]),'COMMA':([13,14,25,27,29,33,49,50,51,52,53,85,86,104,112,113,],[18,-15,-16,18,55,-31,-22,-21,-19,-23,82,-17,107,-20,82,-18,]),'AND':([35,36,37,41,43,45,87,88,89,90,91,92,96,97,],[-48,-38,-43,-46,-45,-47,-44,-37,-39,-42,-41,-40,108,-36,]),'EQUAL':([30,35,36,37,38,41,43,45,84,87,88,89,90,91,92,97,],[56,-48,-38,-43,65,-46,-45,-47,106,-44,-37,-39,-42,-41,-40,-36,]),'STRING_LIT':([24,28,47,56,57,76,79,82,100,103,106,107,],[33,50,33,50,33,33,33,50,33,50,50,33,]),'FROM':([3,12,13,14,15,25,],[11,-13,-14,-15,19,-16,]),'SELECT':([0,],[5,]),'$end':([1,4,6,7,23,46,54,77,102,105,118,],[-1,-2,0,-3,-9,-7,-6,-10,-8,-4,-5,]),'OPENPAR':([16,21,24,31,34,39,47,59,60,61,62,63,64,65,67,68,69,70,72,73,74,75,76,81,108,],[20,28,34,57,34,76,34,34,34,34,34,34,-49,-54,-55,-51,-50,34,34,34,-53,-52,34,103,34,]),'INTO':([2,],[8,]),'IS':([35,36,37,38,41,43,45,87,88,89,90,91,92,97,],[-48,-38,-43,71,-46,-45,-47,-44,-37,-39,-42,-41,-40,-36,]),'LIKE':([33,44,78,],[-31,79,100,]),'MODULO':([35,36,37,41,43,45,87,89,90,91,92,97,],[-48,61,-43,-46,-45,-47,-44,-39,-42,-41,-40,61,]),'ADD':([35,36,37,38,41,43,45,58,87,88,89,90,91,92,94,96,97,115,],[-48,-38,-43,73,-46,-45,-47,73,-44,-37,-39,-42,-41,-40,73,73,-36,73,]),'BETWEEN':([35,36,37,38,41,43,45,87,88,89,90,91,92,97,],[-48,-38,-43,72,-46,-45,-47,-44,-37,-39,-42,-41,-40,-36,]),'DIVIDE_INT':([35,36,37,41,43,45,87,89,90,91,92,97,],[-48,62,-43,-46,-45,-47,-44,-39,-42,-41,-40,62,]),'NE':([35,36,37,38,41,43,45,87,88,89,90,91,92,97,],[-48,-38,-43,74,-46,-45,-47,-44,-37,-39,-42,-41,-40,-36,]),'LT':([35,36,37,38,41,43,45,87,88,89,90,91,92,97,],[-48,-38,-43,75,-46,-45,-47,-44,-37,-39,-42,-41,-40,-36,]),'ASTERISK':([5,35,36,37,41,43,45,87,89,90,91,92,97,],[12,-48,60,-43,-46,-45,-47,-44,-39,-42,-41,-40,60,]),'GE':([35,36,37,38,41,43,45,87,88,89,90,91,92,97,],[-48,-38,-43,64,-46,-45,-47,-44,-37,-39,-42,-41,-40,-36,]),'VALUES':([16,48,],[21,81,]),'DIVIDE':([35,36,37,41,43,45,87,89,90,91,92,97,],[-48,63,-43,-46,-45,-47,-44,-39,-42,-41,-40,63,]),'NOT':([24,33,35,36,37,38,41,43,44,45,47,87,88,89,90,91,92,97,],[39,-31,-48,-38,-43,66,-46,-45,78,-47,39,-44,-37,-39,-42,-41,-40,-36,]),'NULL':([66,71,],[93,95,]),'DELETE':([0,],[3,]),'LE':([35,36,37,38,41,43,45,87,88,89,90,91,92,97,],[-48,-38,-43,68,-46,-45,-47,-44,-37,-39,-42,-41,-40,-36,]),'COLUMN_NAME':([5,18,20,22,24,34,47,55,59,60,61,62,63,64,65,67,68,69,70,72,73,74,75,76,108,],[14,25,14,30,35,35,35,84,35,35,35,35,35,-49,-54,-55,-51,-50,35,35,35,-53,-52,35,35,]),'SET':([16,],[22,]),'SEMICOLON':([17,26,29,32,33,35,36,37,40,41,42,43,45,49,50,52,80,83,85,87,88,89,90,91,92,93,94,95,97,101,109,110,111,113,115,116,117,],[23,46,54,-24,-31,-48,-38,-43,77,-46,-25,-45,-47,-22,-21,-23,102,105,-17,-44,-37,-39,-42,-41,-40,-34,-32,-35,-36,-28,-26,-27,-29,-18,-33,118,-30,]),'EQUAL_NULL':([35,36,37,38,41,43,45,87,88,89,90,91,92,97,],[-48,-38,-43,67,-46,-45,-47,-44,-37,-39,-42,-41,-40,-36,]),'GT':([35,36,37,38,41,43,45,87,88,89,90,91,92,97,],[-48,-38,-43,69,-46,-45,-47,-44,-37,-39,-42,-41,-40,-36,]),'TABLE_NAME':([2,8,9,10,11,19,],[-56,-11,16,-12,17,26,]),'DOUBLE_LIT':([24,28,34,47,56,59,60,61,62,63,64,65,67,68,69,70,72,73,74,75,76,82,103,106,108,],[45,52,45,45,52,45,45,45,45,45,-49,-54,-55,-51,-50,45,45,45,-53,-52,45,52,52,52,45,]),'WHERE':([17,26,],[24,47,]),'CLOSEPAR':([14,25,27,33,35,36,37,41,43,45,49,50,51,52,53,58,87,88,89,90,91,92,93,94,95,97,98,99,101,104,111,112,114,115,117,],[-15,-16,48,-31,-48,-38,-43,-46,-45,-47,-22,-21,-19,-23,83,87,-44,-37,-39,-42,-41,-40,-34,-32,-35,-36,109,110,-28,-20,-29,116,117,-33,-30,]),'SUBTRACT':([35,36,37,41,43,45,87,89,90,91,92,],[-48,59,-43,-46,-45,-47,-44,-39,-42,-41,-40,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'insert_statement':([0,],[1,]),'into_kw':([2,],[9,]),'num_exp':([24,34,47,59,70,72,76,108,],[38,58,38,88,94,96,38,115,]),'select_statement':([0,],[4,]),'string_cond':([24,47,76,],[32,32,98,]),'condition':([24,47,],[40,80,]),'assignment_list':([22,],[29,]),'num_term':([24,34,47,59,60,61,62,63,70,72,73,76,108,],[37,37,37,37,89,90,91,92,37,37,37,37,37,]),'literals':([28,56,82,103,106,],[51,85,104,51,113,]),'num_cond':([24,47,76,],[42,42,99,]),'comparison_op':([38,],[70,]),'statement':([0,],[6,]),'num_factor':([24,34,47,59,70,72,73,76,108,],[36,36,36,36,36,36,97,36,36,]),'num_val':([24,34,47,59,60,61,62,63,70,72,73,76,108,],[43,43,43,43,43,43,43,43,43,43,43,43,43,]),'delete_statement':([0,],[7,]),'columns':([5,],[15,]),'value_list':([28,103,],[53,112,]),'string_exp':([24,47,57,76,79,100,107,],[44,44,86,44,101,111,114,]),'column_name':([5,20,],[13,27,]),'empty':([2,],[10,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> statement","S'",1,None,None,None),
  ('statement -> insert_statement','statement',1,'p_statement','mysqlparse.py',24),
  ('statement -> select_statement','statement',1,'p_statement','mysqlparse.py',25),
  ('statement -> delete_statement','statement',1,'p_statement','mysqlparse.py',26),
  ('insert_statement -> INSERT into_kw TABLE_NAME VALUES OPENPAR value_list CLOSEPAR SEMICOLON','insert_statement',8,'p_insert_statement','mysqlparse.py',29),
  ('insert_statement -> INSERT into_kw TABLE_NAME OPENPAR column_name CLOSEPAR VALUES OPENPAR value_list CLOSEPAR SEMICOLON','insert_statement',11,'p_insert_statement','mysqlparse.py',30),
  ('insert_statement -> INSERT into_kw TABLE_NAME SET assignment_list SEMICOLON','insert_statement',6,'p_insert_statement','mysqlparse.py',31),
  ('select_statement -> SELECT columns FROM TABLE_NAME SEMICOLON','select_statement',5,'p_select_statement','mysqlparse.py',63),
  ('select_statement -> SELECT columns FROM TABLE_NAME WHERE condition SEMICOLON','select_statement',7,'p_select_statement','mysqlparse.py',64),
  ('delete_statement -> DELETE FROM TABLE_NAME SEMICOLON','delete_statement',4,'p_delete_statement','mysqlparse.py',105),
  ('delete_statement -> DELETE FROM TABLE_NAME WHERE condition SEMICOLON','delete_statement',6,'p_delete_statement','mysqlparse.py',106),
  ('into_kw -> INTO','into_kw',1,'p_into_kw','mysqlparse.py',137),
  ('into_kw -> empty','into_kw',1,'p_into_kw','mysqlparse.py',138),
  ('columns -> ASTERISK','columns',1,'p_columns','mysqlparse.py',153),
  ('columns -> column_name','columns',1,'p_columns','mysqlparse.py',154),
  ('column_name -> COLUMN_NAME','column_name',1,'p_column_name','mysqlparse.py',158),
  ('column_name -> column_name COMMA COLUMN_NAME','column_name',3,'p_column_name','mysqlparse.py',159),
  ('assignment_list -> COLUMN_NAME EQUAL literals','assignment_list',3,'p_assignment_list','mysqlparse.py',168),
  ('assignment_list -> assignment_list COMMA COLUMN_NAME EQUAL literals','assignment_list',5,'p_assignment_list','mysqlparse.py',169),
  ('value_list -> literals','value_list',1,'p_value_list','mysqlparse.py',179),
  ('value_list -> value_list COMMA literals','value_list',3,'p_value_list','mysqlparse.py',180),
  ('literals -> STRING_LIT','literals',1,'p_literals','mysqlparse.py',190),
  ('literals -> INT_LIT','literals',1,'p_literals','mysqlparse.py',191),
  ('literals -> DOUBLE_LIT','literals',1,'p_literals','mysqlparse.py',192),
  ('condition -> string_cond','condition',1,'p_condition','mysqlparse.py',196),
  ('condition -> num_cond','condition',1,'p_condition','mysqlparse.py',197),
  ('condition -> NOT OPENPAR string_cond CLOSEPAR','condition',4,'p_condition','mysqlparse.py',198),
  ('condition -> NOT OPENPAR num_cond CLOSEPAR','condition',4,'p_condition','mysqlparse.py',199),
  ('string_cond -> string_exp LIKE string_exp','string_cond',3,'p_string_cond','mysqlparse.py',207),
  ('string_cond -> string_exp NOT LIKE string_exp','string_cond',4,'p_string_cond','mysqlparse.py',208),
  ('string_cond -> STRCMP OPENPAR string_exp COMMA string_exp CLOSEPAR','string_cond',6,'p_string_cond','mysqlparse.py',209),
  ('string_exp -> STRING_LIT','string_exp',1,'p_string_exp','mysqlparse.py',217),
  ('num_cond -> num_exp comparison_op num_exp','num_cond',3,'p_num_cond','mysqlparse.py',223),
  ('num_cond -> num_exp BETWEEN num_exp AND num_exp','num_cond',5,'p_num_cond','mysqlparse.py',224),
  ('num_cond -> num_exp NOT NULL','num_cond',3,'p_num_cond','mysqlparse.py',225),
  ('num_cond -> num_exp IS NULL','num_cond',3,'p_num_cond','mysqlparse.py',226),
  ('num_exp -> num_exp ADD num_factor','num_exp',3,'p_num_exp','mysqlparse.py',281),
  ('num_exp -> num_factor SUBTRACT num_exp','num_exp',3,'p_num_exp','mysqlparse.py',282),
  ('num_exp -> num_factor','num_exp',1,'p_num_exp','mysqlparse.py',283),
  ('num_factor -> num_factor ASTERISK num_term','num_factor',3,'p_num_factor','mysqlparse.py',297),
  ('num_factor -> num_factor DIVIDE num_term','num_factor',3,'p_num_factor','mysqlparse.py',298),
  ('num_factor -> num_factor DIVIDE_INT num_term','num_factor',3,'p_num_factor','mysqlparse.py',299),
  ('num_factor -> num_factor MODULO num_term','num_factor',3,'p_num_factor','mysqlparse.py',300),
  ('num_factor -> num_term','num_factor',1,'p_num_factor','mysqlparse.py',301),
  ('num_term -> OPENPAR num_exp CLOSEPAR','num_term',3,'p_num_term','mysqlparse.py',318),
  ('num_term -> num_val','num_term',1,'p_num_term','mysqlparse.py',319),
  ('num_val -> INT_LIT','num_val',1,'p_num_val','mysqlparse.py',329),
  ('num_val -> DOUBLE_LIT','num_val',1,'p_num_val','mysqlparse.py',330),
  ('num_val -> COLUMN_NAME','num_val',1,'p_num_val','mysqlparse.py',331),
  ('comparison_op -> GE','comparison_op',1,'p_comparison_op','mysqlparse.py',340),
  ('comparison_op -> GT','comparison_op',1,'p_comparison_op','mysqlparse.py',341),
  ('comparison_op -> LE','comparison_op',1,'p_comparison_op','mysqlparse.py',342),
  ('comparison_op -> LT','comparison_op',1,'p_comparison_op','mysqlparse.py',343),
  ('comparison_op -> NE','comparison_op',1,'p_comparison_op','mysqlparse.py',344),
  ('comparison_op -> EQUAL','comparison_op',1,'p_comparison_op','mysqlparse.py',345),
  ('comparison_op -> EQUAL_NULL','comparison_op',1,'p_comparison_op','mysqlparse.py',346),
  ('empty -> <empty>','empty',0,'p_empty','mysqlparse.py',351),
]
