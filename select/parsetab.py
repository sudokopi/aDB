
# parsetab.py
# This file is automatically generated. Do not edit.
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftADDSUBTRACTleftMULTIPLYDIVIDEDIVIDE_INTFROM WHERE SELECT DELETE LIKE STRCMP IS NULL BETWEEN AND ADDDATE CURDATE CURRENT_DATE DATEDIFF DAY DAYNAME DAYOFMONTH DAYOFWEEK DAYOFYEAR LAST_DAY MAKEDATE MONTH MONTHNAME SUBDATE INTERVAL YEAR COLUMN_NAME TABLE_NAME FILTER_ROWS INT_LIT DOUBLE_LIT STRING_LIT DATE_LIT ASTERISK DATE_UNIT COMMA SEMICOLON ADD SUBTRACT MULTIPLY DIVIDE DIVIDE_INT MODULO EQUAL EQUAL_NULL GT GE LT LE NE NOT OPENPAR CLOSEPARstatement : delete_statement\n            | select_statementselect_statement : SELECT filter_rows_op columns FROM TABLE_NAME SEMICOLON\n            | SELECT filter_rows_op columns FROM TABLE_NAME WHERE condition SEMICOLONdelete_statement : DELETE FROM TABLE_NAME SEMICOLON\n            | DELETE FROM TABLE_NAME WHERE condition SEMICOLONfilter_rows_op : FILTER_ROWS\n            | emptycolumns : ASTERISK\n            | column_namecolumn_name : COLUMN_NAME\n            | column_name COMMA COLUMN_NAMEcondition : string_cond\n            | num_cond\n            | date_cond\n            | NOT OPENPAR string_cond CLOSEPAR\n            | NOT OPENPAR num_cond CLOSEPAR\n            | NOT OPENPAR date_cond CLOSEPARstring_cond : string_exp LIKE string_exp\n            | string_exp NOT LIKE string_exp\n            | STRCMP OPENPAR string_exp COMMA string_exp CLOSEPARstring_exp : STRING_LITnum_cond : num_exp comparison_op num_exp\n            | num_exp BETWEEN num_exp AND num_exp\n            | num_exp NOT NULL\n            | num_exp IS NULLnum_exp : num_exp ADD num_factor\n            | num_exp SUBTRACT num_factor\n            | num_factornum_factor : num_factor MULTIPLY num_term\n            | num_factor DIVIDE num_term\n            | num_factor DIVIDE_INT num_term\n            | num_factor MODULO num_term\n            | num_termnum_term : OPENPAR num_val CLOSEPAR\n            | num_valnum_val : INT_LIT\n            | DOUBLE_LIT\n            | COLUMN_NAMEdate_cond : date_exp comparison_op date_exp\n            | date_expdate_exp : date_function\n            | DATE_LITdate_function : ADDDATE OPENPAR date_exp COMMA date_exp CLOSEPAR\n             | CURDATE OPENPAR CLOSEPAR\n             | CURRENT_DATE OPENPAR CLOSEPAR\n             | CURRENT_DATE\n             | DATEDIFF OPENPAR date_exp COMMA date_exp CLOSEPAR\n             | DAY OPENPAR date_exp CLOSEPAR\n             | DAYNAME OPENPAR date_exp CLOSEPAR\n             | DAYOFMONTH OPENPAR date_exp CLOSEPAR\n             | DAYOFWEEK OPENPAR date_exp CLOSEPAR\n             | DAYOFYEAR OPENPAR date_exp CLOSEPAR\n             | LAST_DAY OPENPAR date_exp CLOSEPAR\n             | MAKEDATE OPENPAR num_exp COMMA num_exp CLOSEPAR\n             | MONTH OPENPAR date_exp CLOSEPAR\n             | MONTHNAME OPENPAR date_exp CLOSEPAR\n             | SUBDATE OPENPAR date_exp COMMA INTERVAL num_exp DATE_UNIT CLOSEPAR\n             | YEAR OPENPAR date_exp CLOSEPARcomparison_op : GE\n            | GT\n            | LE\n            | LT\n            | NE\n            | EQUAL\n            | EQUAL_NULLempty : '
    
_lr_action_items = {'DAYOFWEEK':([16,55,57,58,59,60,65,66,67,69,70,71,73,78,80,82,83,89,90,91,92,93,94,138,144,],[19,19,-63,-60,-65,-62,-66,-61,-64,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,]),'GE':([21,22,25,26,30,31,32,37,40,42,44,97,100,108,113,115,120,121,122,123,130,132,133,134,139,143,146,147,148,156,158,159,162,],[-37,58,-34,-43,58,-42,-47,-38,-39,-36,-29,-28,-27,-46,-35,-45,-30,-32,-31,-33,-52,-57,-51,-59,-53,-56,-49,-50,-54,-55,-44,-48,-58,]),'DAY':([16,55,57,58,59,60,65,66,67,69,70,71,73,78,80,82,83,89,90,91,92,93,94,138,144,],[50,50,-63,-60,-65,-62,-66,-61,-64,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,]),'MAKEDATE':([16,55,57,58,59,60,65,66,67,69,70,71,73,78,80,82,83,89,90,91,92,93,94,138,144,],[29,29,-63,-60,-65,-62,-66,-61,-64,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,]),'SELECT':([0,],[2,]),'DAYOFYEAR':([16,55,57,58,59,60,65,66,67,69,70,71,73,78,80,82,83,89,90,91,92,93,94,138,144,],[38,38,-63,-60,-65,-62,-66,-61,-64,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,]),'DOUBLE_LIT':([16,36,56,57,58,59,60,61,63,64,65,66,67,72,82,84,85,86,87,94,131,135,155,],[37,37,37,-63,-60,-65,-62,37,37,37,-66,-61,-64,37,37,37,37,37,37,37,37,37,37,]),'EQUAL_NULL':([21,22,25,26,30,31,32,37,40,42,44,97,100,108,113,115,120,121,122,123,130,132,133,134,139,143,146,147,148,156,158,159,162,],[-37,65,-34,-43,65,-42,-47,-38,-39,-36,-29,-28,-27,-46,-35,-45,-30,-32,-31,-33,-52,-57,-51,-59,-53,-56,-49,-50,-54,-55,-44,-48,-58,]),'ADDDATE':([16,55,57,58,59,60,65,66,67,69,70,71,73,78,80,82,83,89,90,91,92,93,94,138,144,],[35,35,-63,-60,-65,-62,-66,-61,-64,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,]),'$end':([3,4,5,15,88,95,149,],[-1,0,-2,-5,-6,-3,-4,]),'DAYOFMONTH':([16,55,57,58,59,60,65,66,67,69,70,71,73,78,80,82,83,89,90,91,92,93,94,138,144,],[27,27,-63,-60,-65,-62,-66,-61,-64,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,]),'WHERE':([10,54,],[16,94,]),'SUBTRACT':([21,22,25,37,40,42,44,97,98,100,101,106,113,120,121,122,123,150,151,160,],[-37,56,-34,-38,-39,-36,-29,-28,56,-27,56,56,-35,-30,-32,-31,-33,56,56,56,]),'EQUAL':([21,22,25,26,30,31,32,37,40,42,44,97,100,108,113,115,120,121,122,123,130,132,133,134,139,143,146,147,148,156,158,159,162,],[-37,59,-34,-43,59,-42,-47,-38,-39,-36,-29,-28,-27,-46,-35,-45,-30,-32,-31,-33,-52,-57,-51,-59,-53,-56,-49,-50,-54,-55,-44,-48,-58,]),'DATE_LIT':([16,55,57,58,59,60,65,66,67,69,70,71,73,78,80,82,83,89,90,91,92,93,94,138,144,],[26,26,-63,-60,-65,-62,-66,-61,-64,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,]),'DATE_UNIT':([21,25,37,40,42,44,97,100,113,120,121,122,123,160,],[-37,-34,-38,-39,-36,-29,-28,-27,-35,-30,-32,-31,-33,161,]),'TABLE_NAME':([6,18,],[10,54,]),'YEAR':([16,55,57,58,59,60,65,66,67,69,70,71,73,78,80,82,83,89,90,91,92,93,94,138,144,],[28,28,-63,-60,-65,-62,-66,-61,-64,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,]),'LT':([21,22,25,26,30,31,32,37,40,42,44,97,100,108,113,115,120,121,122,123,130,132,133,134,139,143,146,147,148,156,158,159,162,],[-37,57,-34,-43,57,-42,-47,-38,-39,-36,-29,-28,-27,-46,-35,-45,-30,-32,-31,-33,-52,-57,-51,-59,-53,-56,-49,-50,-54,-55,-44,-48,-58,]),'ADD':([21,22,25,37,40,42,44,97,98,100,101,106,113,120,121,122,123,150,151,160,],[-37,63,-34,-38,-39,-36,-29,-28,63,-27,63,63,-35,-30,-32,-31,-33,63,63,63,]),'CURRENT_DATE':([16,55,57,58,59,60,65,66,67,69,70,71,73,78,80,82,83,89,90,91,92,93,94,138,144,],[32,32,-63,-60,-65,-62,-66,-61,-64,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,]),'STRCMP':([16,82,94,],[34,34,34,]),'LE':([21,22,25,26,30,31,32,37,40,42,44,97,100,108,113,115,120,121,122,123,130,132,133,134,139,143,146,147,148,156,158,159,162,],[-37,60,-34,-43,60,-42,-47,-38,-39,-36,-29,-28,-27,-46,-35,-45,-30,-32,-31,-33,-52,-57,-51,-59,-53,-56,-49,-50,-54,-55,-44,-48,-58,]),'SEMICOLON':([10,20,21,24,25,26,30,31,32,37,40,42,44,45,47,49,54,97,99,100,101,102,107,108,109,113,115,120,121,122,123,129,130,132,133,134,136,139,140,141,142,143,146,147,148,150,156,157,158,159,162,],[15,-15,-37,-13,-34,-43,-41,-42,-47,-38,-39,-36,-29,88,-22,-14,95,-28,-26,-27,-23,-25,-40,-46,-19,-35,-45,-30,-32,-31,-33,149,-52,-57,-51,-59,-20,-53,-18,-16,-17,-56,-49,-50,-54,-24,-55,-21,-44,-48,-58,]),'SUBDATE':([16,55,57,58,59,60,65,66,67,69,70,71,73,78,80,82,83,89,90,91,92,93,94,138,144,],[48,48,-63,-60,-65,-62,-66,-61,-64,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,]),'NE':([21,22,25,26,30,31,32,37,40,42,44,97,100,108,113,115,120,121,122,123,130,132,133,134,139,143,146,147,148,156,158,159,162,],[-37,67,-34,-43,67,-42,-47,-38,-39,-36,-29,-28,-27,-46,-35,-45,-30,-32,-31,-33,-52,-57,-51,-59,-53,-56,-49,-50,-54,-55,-44,-48,-58,]),'DIVIDE_INT':([21,25,37,40,42,44,97,100,113,120,121,122,123,],[-37,-34,-38,-39,-36,85,85,85,-35,-30,-32,-31,-33,]),'CLOSEPAR':([21,25,26,30,31,32,37,40,42,44,47,74,79,81,96,97,99,100,101,102,103,104,105,107,108,109,113,114,115,116,117,118,119,120,121,122,123,126,127,128,130,132,133,134,136,139,143,146,147,148,150,151,152,153,154,156,157,158,159,161,162,],[-37,-34,-43,-41,-42,-47,-38,-39,-36,-29,-22,108,113,115,130,-28,-26,-27,-23,-25,132,133,134,-40,-46,-19,-35,139,-45,140,141,142,143,-30,-32,-31,-33,146,147,148,-52,-57,-51,-59,-20,-53,-56,-49,-50,-54,-24,156,157,158,159,-55,-21,-44,-48,162,-58,]),'OPENPAR':([16,19,23,27,28,29,32,34,35,38,39,41,43,46,48,50,51,52,56,57,58,59,60,61,63,64,65,66,67,72,82,84,85,86,87,94,131,135,155,],[36,55,69,70,71,72,74,77,78,80,81,82,83,89,90,91,92,93,36,-63,-60,-65,-62,36,36,36,-66,-61,-64,36,36,36,36,36,36,36,36,36,36,]),'NULL':([62,68,],[99,102,]),'DELETE':([0,],[1,]),'COMMA':([11,13,21,25,26,31,32,37,40,42,44,47,53,97,100,106,108,111,112,113,115,120,121,122,123,124,125,130,132,133,134,139,143,146,147,148,156,158,159,162,],[17,-11,-37,-34,-43,-42,-47,-38,-39,-36,-29,-22,-12,-28,-27,135,-46,137,138,-35,-45,-30,-32,-31,-33,144,145,-52,-57,-51,-59,-53,-56,-49,-50,-54,-55,-44,-48,-58,]),'FILTER_ROWS':([2,],[7,]),'IS':([21,22,25,37,40,42,44,97,100,113,120,121,122,123,],[-37,62,-34,-38,-39,-36,-29,-28,-27,-35,-30,-32,-31,-33,]),'CURDATE':([16,55,57,58,59,60,65,66,67,69,70,71,73,78,80,82,83,89,90,91,92,93,94,138,144,],[39,39,-63,-60,-65,-62,-66,-61,-64,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,]),'INT_LIT':([16,36,56,57,58,59,60,61,63,64,65,66,67,72,82,84,85,86,87,94,131,135,155,],[21,21,21,-63,-60,-65,-62,21,21,21,-66,-61,-64,21,21,21,21,21,21,21,21,21,21,]),'COLUMN_NAME':([2,7,8,9,16,17,36,56,57,58,59,60,61,63,64,65,66,67,72,82,84,85,86,87,94,131,135,155,],[-67,-7,13,-8,40,53,40,40,-63,-60,-65,-62,40,40,40,-66,-61,-64,40,40,40,40,40,40,40,40,40,40,]),'NOT':([16,21,22,25,33,37,40,42,44,47,94,97,100,113,120,121,122,123,],[41,-37,68,-34,76,-38,-39,-36,-29,-22,41,-28,-27,-35,-30,-32,-31,-33,]),'INTERVAL':([145,],[155,]),'MONTH':([16,55,57,58,59,60,65,66,67,69,70,71,73,78,80,82,83,89,90,91,92,93,94,138,144,],[43,43,-63,-60,-65,-62,-66,-61,-64,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,]),'MULTIPLY':([21,25,37,40,42,44,97,100,113,120,121,122,123,],[-37,-34,-38,-39,-36,84,84,84,-35,-30,-32,-31,-33,]),'DATEDIFF':([16,55,57,58,59,60,65,66,67,69,70,71,73,78,80,82,83,89,90,91,92,93,94,138,144,],[46,46,-63,-60,-65,-62,-66,-61,-64,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,]),'BETWEEN':([21,22,25,37,40,42,44,97,100,113,120,121,122,123,],[-37,61,-34,-38,-39,-36,-29,-28,-27,-35,-30,-32,-31,-33,]),'MONTHNAME':([16,55,57,58,59,60,65,66,67,69,70,71,73,78,80,82,83,89,90,91,92,93,94,138,144,],[23,23,-63,-60,-65,-62,-66,-61,-64,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,]),'STRING_LIT':([16,75,77,82,94,110,137,],[47,47,47,47,47,47,47,]),'ASTERISK':([2,7,8,9,],[-67,-7,14,-8,]),'GT':([21,22,25,26,30,31,32,37,40,42,44,97,100,108,113,115,120,121,122,123,130,132,133,134,139,143,146,147,148,156,158,159,162,],[-37,66,-34,-43,66,-42,-47,-38,-39,-36,-29,-28,-27,-46,-35,-45,-30,-32,-31,-33,-52,-57,-51,-59,-53,-56,-49,-50,-54,-55,-44,-48,-58,]),'MODULO':([21,25,37,40,42,44,97,100,113,120,121,122,123,],[-37,-34,-38,-39,-36,87,87,87,-35,-30,-32,-31,-33,]),'LIKE':([33,47,76,],[75,-22,110,]),'DIVIDE':([21,25,37,40,42,44,97,100,113,120,121,122,123,],[-37,-34,-38,-39,-36,86,86,86,-35,-30,-32,-31,-33,]),'DAYNAME':([16,55,57,58,59,60,65,66,67,69,70,71,73,78,80,82,83,89,90,91,92,93,94,138,144,],[51,51,-63,-60,-65,-62,-66,-61,-64,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,]),'FROM':([1,11,12,13,14,53,],[6,-10,18,-11,-9,-12,]),'LAST_DAY':([16,55,57,58,59,60,65,66,67,69,70,71,73,78,80,82,83,89,90,91,92,93,94,138,144,],[52,52,-63,-60,-65,-62,-66,-61,-64,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,]),'AND':([21,25,37,40,42,44,97,98,100,113,120,121,122,123,],[-37,-34,-38,-39,-36,-29,-28,131,-27,-35,-30,-32,-31,-33,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'num_exp':([16,61,64,72,82,94,131,135,155,],[22,98,101,106,22,22,150,151,160,]),'column_name':([8,],[11,]),'num_factor':([16,56,61,63,64,72,82,94,131,135,155,],[44,97,44,100,44,44,44,44,44,44,44,]),'date_cond':([16,82,94,],[20,116,20,]),'empty':([2,],[9,]),'condition':([16,94,],[45,129,]),'filter_rows_op':([2,],[8,]),'columns':([8,],[12,]),'date_exp':([16,55,69,70,71,73,78,80,82,83,89,90,91,92,93,94,138,144,],[30,96,103,104,105,107,112,114,30,119,124,125,126,127,128,30,153,154,]),'num_val':([16,36,56,61,63,64,72,82,84,85,86,87,94,131,135,155,],[42,79,42,42,42,42,42,42,42,42,42,42,42,42,42,42,]),'comparison_op':([22,30,],[64,73,]),'date_function':([16,55,69,70,71,73,78,80,82,83,89,90,91,92,93,94,138,144,],[31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,]),'statement':([0,],[4,]),'num_cond':([16,82,94,],[49,118,49,]),'string_exp':([16,75,77,82,94,110,137,],[33,109,111,33,33,136,152,]),'delete_statement':([0,],[3,]),'string_cond':([16,82,94,],[24,117,24,]),'select_statement':([0,],[5,]),'num_term':([16,56,61,63,64,72,82,84,85,86,87,94,131,135,155,],[25,25,25,25,25,25,25,120,121,122,123,25,25,25,25,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> statement","S'",1,None,None,None),
  ('statement -> delete_statement','statement',1,'p_statement','select.py',152),
  ('statement -> select_statement','statement',1,'p_statement','select.py',153),
  ('select_statement -> SELECT filter_rows_op columns FROM TABLE_NAME SEMICOLON','select_statement',6,'p_select_statement','select.py',156),
  ('select_statement -> SELECT filter_rows_op columns FROM TABLE_NAME WHERE condition SEMICOLON','select_statement',8,'p_select_statement','select.py',157),
  ('delete_statement -> DELETE FROM TABLE_NAME SEMICOLON','delete_statement',4,'p_delete_statement','select.py',160),
  ('delete_statement -> DELETE FROM TABLE_NAME WHERE condition SEMICOLON','delete_statement',6,'p_delete_statement','select.py',161),
  ('filter_rows_op -> FILTER_ROWS','filter_rows_op',1,'p_filter_rows_op','select.py',164),
  ('filter_rows_op -> empty','filter_rows_op',1,'p_filter_rows_op','select.py',165),
  ('columns -> ASTERISK','columns',1,'p_columns','select.py',168),
  ('columns -> column_name','columns',1,'p_columns','select.py',169),
  ('column_name -> COLUMN_NAME','column_name',1,'p_column_name','select.py',173),
  ('column_name -> column_name COMMA COLUMN_NAME','column_name',3,'p_column_name','select.py',174),
  ('condition -> string_cond','condition',1,'p_condition','select.py',177),
  ('condition -> num_cond','condition',1,'p_condition','select.py',178),
  ('condition -> date_cond','condition',1,'p_condition','select.py',179),
  ('condition -> NOT OPENPAR string_cond CLOSEPAR','condition',4,'p_condition','select.py',180),
  ('condition -> NOT OPENPAR num_cond CLOSEPAR','condition',4,'p_condition','select.py',181),
  ('condition -> NOT OPENPAR date_cond CLOSEPAR','condition',4,'p_condition','select.py',182),
  ('string_cond -> string_exp LIKE string_exp','string_cond',3,'p_string_cond','select.py',186),
  ('string_cond -> string_exp NOT LIKE string_exp','string_cond',4,'p_string_cond','select.py',187),
  ('string_cond -> STRCMP OPENPAR string_exp COMMA string_exp CLOSEPAR','string_cond',6,'p_string_cond','select.py',188),
  ('string_exp -> STRING_LIT','string_exp',1,'p_string_exp','select.py',193),
  ('num_cond -> num_exp comparison_op num_exp','num_cond',3,'p_num_cond','select.py',198),
  ('num_cond -> num_exp BETWEEN num_exp AND num_exp','num_cond',5,'p_num_cond','select.py',199),
  ('num_cond -> num_exp NOT NULL','num_cond',3,'p_num_cond','select.py',200),
  ('num_cond -> num_exp IS NULL','num_cond',3,'p_num_cond','select.py',201),
  ('num_exp -> num_exp ADD num_factor','num_exp',3,'p_num_exp','select.py',204),
  ('num_exp -> num_exp SUBTRACT num_factor','num_exp',3,'p_num_exp','select.py',205),
  ('num_exp -> num_factor','num_exp',1,'p_num_exp','select.py',206),
  ('num_factor -> num_factor MULTIPLY num_term','num_factor',3,'p_num_factor','select.py',209),
  ('num_factor -> num_factor DIVIDE num_term','num_factor',3,'p_num_factor','select.py',210),
  ('num_factor -> num_factor DIVIDE_INT num_term','num_factor',3,'p_num_factor','select.py',211),
  ('num_factor -> num_factor MODULO num_term','num_factor',3,'p_num_factor','select.py',212),
  ('num_factor -> num_term','num_factor',1,'p_num_factor','select.py',213),
  ('num_term -> OPENPAR num_val CLOSEPAR','num_term',3,'p_num_term','select.py',216),
  ('num_term -> num_val','num_term',1,'p_num_term','select.py',217),
  ('num_val -> INT_LIT','num_val',1,'p_num_val','select.py',220),
  ('num_val -> DOUBLE_LIT','num_val',1,'p_num_val','select.py',221),
  ('num_val -> COLUMN_NAME','num_val',1,'p_num_val','select.py',222),
  ('date_cond -> date_exp comparison_op date_exp','date_cond',3,'p_date_cond','select.py',225),
  ('date_cond -> date_exp','date_cond',1,'p_date_cond','select.py',226),
  ('date_exp -> date_function','date_exp',1,'p_date_exp','select.py',229),
  ('date_exp -> DATE_LIT','date_exp',1,'p_date_exp','select.py',230),
  ('date_function -> ADDDATE OPENPAR date_exp COMMA date_exp CLOSEPAR','date_function',6,'p_date_function','select.py',233),
  ('date_function -> CURDATE OPENPAR CLOSEPAR','date_function',3,'p_date_function','select.py',234),
  ('date_function -> CURRENT_DATE OPENPAR CLOSEPAR','date_function',3,'p_date_function','select.py',235),
  ('date_function -> CURRENT_DATE','date_function',1,'p_date_function','select.py',236),
  ('date_function -> DATEDIFF OPENPAR date_exp COMMA date_exp CLOSEPAR','date_function',6,'p_date_function','select.py',237),
  ('date_function -> DAY OPENPAR date_exp CLOSEPAR','date_function',4,'p_date_function','select.py',238),
  ('date_function -> DAYNAME OPENPAR date_exp CLOSEPAR','date_function',4,'p_date_function','select.py',239),
  ('date_function -> DAYOFMONTH OPENPAR date_exp CLOSEPAR','date_function',4,'p_date_function','select.py',240),
  ('date_function -> DAYOFWEEK OPENPAR date_exp CLOSEPAR','date_function',4,'p_date_function','select.py',241),
  ('date_function -> DAYOFYEAR OPENPAR date_exp CLOSEPAR','date_function',4,'p_date_function','select.py',242),
  ('date_function -> LAST_DAY OPENPAR date_exp CLOSEPAR','date_function',4,'p_date_function','select.py',243),
  ('date_function -> MAKEDATE OPENPAR num_exp COMMA num_exp CLOSEPAR','date_function',6,'p_date_function','select.py',244),
  ('date_function -> MONTH OPENPAR date_exp CLOSEPAR','date_function',4,'p_date_function','select.py',245),
  ('date_function -> MONTHNAME OPENPAR date_exp CLOSEPAR','date_function',4,'p_date_function','select.py',246),
  ('date_function -> SUBDATE OPENPAR date_exp COMMA INTERVAL num_exp DATE_UNIT CLOSEPAR','date_function',8,'p_date_function','select.py',247),
  ('date_function -> YEAR OPENPAR date_exp CLOSEPAR','date_function',4,'p_date_function','select.py',248),
  ('comparison_op -> GE','comparison_op',1,'p_comparison_op','select.py',251),
  ('comparison_op -> GT','comparison_op',1,'p_comparison_op','select.py',252),
  ('comparison_op -> LE','comparison_op',1,'p_comparison_op','select.py',253),
  ('comparison_op -> LT','comparison_op',1,'p_comparison_op','select.py',254),
  ('comparison_op -> NE','comparison_op',1,'p_comparison_op','select.py',255),
  ('comparison_op -> EQUAL','comparison_op',1,'p_comparison_op','select.py',256),
  ('comparison_op -> EQUAL_NULL','comparison_op',1,'p_comparison_op','select.py',257),
  ('empty -> <empty>','empty',0,'p_empty','select.py',268),
]
