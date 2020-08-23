import os
import sys
import pickle

from pyparsing import *

from . import schema
from .nodes import *

def parse(fn):

    cache_file = fn + ".cache.dat"
    if os.path.exists(cache_file):
        with open(cache_file, "rb") as f:
            s = pickle.load(f)
    else:
        ABS = (CaselessKeyword("abs"))
        ABSTRACT = (CaselessKeyword("abstract"))
        ACOS = (CaselessKeyword("acos"))
        AGGREGATE = (CaselessKeyword("aggregate"))
        ALIAS = (CaselessKeyword("alias"))
        AND = (CaselessKeyword("and"))
        ANDOR = (CaselessKeyword("andor"))
        ARRAY = (CaselessKeyword("array"))
        AS = (CaselessKeyword("as"))
        ASIN = (CaselessKeyword("asin"))
        ATAN = (CaselessKeyword("atan"))
        BAG = (CaselessKeyword("bag"))
        BASED_ON = (CaselessKeyword("based_on"))
        BEGIN = (CaselessKeyword("begin"))
        BINARY = (CaselessKeyword("binary"))
        BLENGTH = (CaselessKeyword("blength"))
        BOOLEAN = (CaselessKeyword("boolean"))
        BY = (CaselessKeyword("by"))
        CASE = (CaselessKeyword("case"))
        CONSTANT = (CaselessKeyword("constant"))
        CONST_E = (CaselessKeyword("const_e"))
        COS = (CaselessKeyword("cos"))
        DERIVE = (CaselessKeyword("derive"))
        DIV = (CaselessKeyword("div"))
        ELSE = (CaselessKeyword("else"))
        END = (CaselessKeyword("end"))
        END_ALIAS = (CaselessKeyword("end_alias"))
        END_CASE = (CaselessKeyword("end_case"))
        END_CONSTANT = (CaselessKeyword("end_constant"))
        END_ENTITY = (CaselessKeyword("end_entity"))
        END_FUNCTION = (CaselessKeyword("end_function"))
        END_IF = (CaselessKeyword("end_if"))
        END_LOCAL = (CaselessKeyword("end_local"))
        END_PROCEDURE = (CaselessKeyword("end_procedure"))
        END_REPEAT = (CaselessKeyword("end_repeat"))
        END_RULE = (CaselessKeyword("end_rule"))
        END_SCHEMA = (CaselessKeyword("end_schema"))
        END_SUBTYPE_CONSTRAINT = (CaselessKeyword("end_subtype_constraint"))
        END_TYPE = (CaselessKeyword("end_type"))
        ENTITY = (CaselessKeyword("entity"))
        ENUMERATION = (CaselessKeyword("enumeration"))
        ESCAPE = (CaselessKeyword("escape"))
        EXISTS = (CaselessKeyword("exists"))
        EXTENSIBLE = (CaselessKeyword("extensible"))
        EXP = (CaselessKeyword("exp"))
        FALSE = (CaselessKeyword("false"))
        FIXED = (CaselessKeyword("fixed"))
        FOR = (CaselessKeyword("for"))
        FORMAT = (CaselessKeyword("format"))
        FROM = (CaselessKeyword("from"))
        FUNCTION = (CaselessKeyword("function"))
        GENERIC = (CaselessKeyword("generic"))
        GENERIC_ENTITY = (CaselessKeyword("generic_entity"))
        HIBOUND = (CaselessKeyword("hibound"))
        HIINDEX = (CaselessKeyword("hiindex"))
        IF = (CaselessKeyword("if"))
        IN = (CaselessKeyword("in"))
        INSERT = (CaselessKeyword("insert"))
        INTEGER = (CaselessKeyword("integer"))
        INVERSE = (CaselessKeyword("inverse"))
        LENGTH = (CaselessKeyword("length"))
        LIKE = (CaselessKeyword("like"))
        LIST = (CaselessKeyword("list"))
        LOBOUND = (CaselessKeyword("lobound"))
        LOCAL = (CaselessKeyword("local"))
        LOG = (CaselessKeyword("log"))
        LOG10 = (CaselessKeyword("log10"))
        LOG2 = (CaselessKeyword("log2"))
        LOGICAL = (CaselessKeyword("logical"))
        LOINDEX = (CaselessKeyword("loindex"))
        MOD = (CaselessKeyword("mod"))
        NOT = (CaselessKeyword("not"))
        NUMBER = (CaselessKeyword("number"))
        NVL = (CaselessKeyword("nvl"))
        ODD = (CaselessKeyword("odd"))
        OF = (CaselessKeyword("of"))
        ONEOF = (CaselessKeyword("oneof"))
        OPTIONAL = (CaselessKeyword("optional"))
        OR = (CaselessKeyword("or"))
        OTHERWISE = (CaselessKeyword("otherwise"))
        PI = (CaselessKeyword("pi"))
        PROCEDURE = (CaselessKeyword("procedure"))
        QUERY = (CaselessKeyword("query"))
        REAL = (CaselessKeyword("real"))
        REFERENCE = (CaselessKeyword("reference"))
        REMOVE = (CaselessKeyword("remove"))
        RENAMED = (CaselessKeyword("renamed"))
        REPEAT = (CaselessKeyword("repeat"))
        RETURN = (CaselessKeyword("return"))
        ROLESOF = (CaselessKeyword("rolesof"))
        RULE = (CaselessKeyword("rule"))
        SCHEMA = (CaselessKeyword("schema"))
        SELECT = (CaselessKeyword("select"))
        SELF = (CaselessKeyword("self"))
        SET = (CaselessKeyword("set"))
        SIN = (CaselessKeyword("sin"))
        SIZEOF = (CaselessKeyword("sizeof"))
        SKIP = (CaselessKeyword("skip"))
        SQRT = (CaselessKeyword("sqrt"))
        STRING = (CaselessKeyword("string"))
        SUBTYPE = (CaselessKeyword("subtype"))
        SUBTYPE_CONSTRAINT = (CaselessKeyword("subtype_constraint"))
        SUPERTYPE = (CaselessKeyword("supertype"))
        TAN = (CaselessKeyword("tan"))
        THEN = (CaselessKeyword("then"))
        TO = (CaselessKeyword("to"))
        TOTAL_OVER = (CaselessKeyword("total_over"))
        TRUE = (CaselessKeyword("true"))
        TYPE = (CaselessKeyword("type"))
        TYPEOF = (CaselessKeyword("typeof"))
        UNIQUE = (CaselessKeyword("unique"))
        UNKNOWN = (CaselessKeyword("unknown"))
        UNTIL = (CaselessKeyword("until"))
        USE = (CaselessKeyword("use"))
        USEDIN = (CaselessKeyword("usedin"))
        VALUE = (CaselessKeyword("value"))
        VALUE_IN = (CaselessKeyword("value_in"))
        VALUE_UNIQUE = (CaselessKeyword("value_unique"))
        VAR = (CaselessKeyword("var"))
        WHERE = (CaselessKeyword("where"))
        WHILE = (CaselessKeyword("while"))
        WITH = (CaselessKeyword("with"))
        XOR = (CaselessKeyword("xor"))
        bit = ((CaselessLiteral("0") | CaselessLiteral("1")))
        digit = ((CaselessLiteral("0") | CaselessLiteral("1") | CaselessLiteral("2") | CaselessLiteral("3") | CaselessLiteral("4") | CaselessLiteral("5") | CaselessLiteral("6") | CaselessLiteral("7") | CaselessLiteral("8") | CaselessLiteral("9")))
        digits = ((digit + ZeroOrMore(digit)))
        hex_digit = ((digit | CaselessLiteral("a") | CaselessLiteral("b") | CaselessLiteral("c") | CaselessLiteral("d") | CaselessLiteral("e") | CaselessLiteral("f")))
        letter = ((CaselessLiteral("a") | CaselessLiteral("b") | CaselessLiteral("c") | CaselessLiteral("d") | CaselessLiteral("e") | CaselessLiteral("f") | CaselessLiteral("g") | CaselessLiteral("h") | CaselessLiteral("i") | CaselessLiteral("j") | CaselessLiteral("k") | CaselessLiteral("l") | CaselessLiteral("m") | CaselessLiteral("n") | CaselessLiteral("o") | CaselessLiteral("p") | CaselessLiteral("q") | CaselessLiteral("r") | CaselessLiteral("s") | CaselessLiteral("t") | CaselessLiteral("u") | CaselessLiteral("v") | CaselessLiteral("w") | CaselessLiteral("x") | CaselessLiteral("y") | CaselessLiteral("z")))
        not_paren_star_quote_special = ((CaselessLiteral("!") | CaselessLiteral("#") | CaselessLiteral("$") | CaselessLiteral("%") | CaselessLiteral("&") | CaselessLiteral("+") | CaselessLiteral(",") | CaselessLiteral("-") | CaselessLiteral(".") | CaselessLiteral("/") | CaselessLiteral(":") | CaselessLiteral(";") | CaselessLiteral("<") | CaselessLiteral("=") | CaselessLiteral(">") | CaselessLiteral("?") | CaselessLiteral("@") | CaselessLiteral("[") | CaselessLiteral("\\") | CaselessLiteral("]") | CaselessLiteral("^") | CaselessLiteral("_") | CaselessLiteral("{") | CaselessLiteral("|") | CaselessLiteral("}") | CaselessLiteral("~")))
        not_paren_star_special = ((not_paren_star_quote_special | CaselessLiteral("\"\"")))
        not_quote = ((not_paren_star_quote_special | letter | digit | CaselessLiteral("(") | CaselessLiteral(")") | CaselessLiteral("*")))
        octet = ((hex_digit + hex_digit))
        special = ((not_paren_star_quote_special | CaselessLiteral("(") | CaselessLiteral(")") | CaselessLiteral("*") | CaselessLiteral("\"\"")))
        binary_literal = ((CaselessLiteral("%") + bit + ZeroOrMore(bit)))
        integer_literal = (digits)
        simple_id = ~CaselessKeyword("with") + ~CaselessKeyword("array") + ~CaselessKeyword("asin") + ~CaselessKeyword("abstract") + ~CaselessKeyword("abs") + ~CaselessKeyword("extensible") + ~CaselessKeyword("case") + ~CaselessKeyword("end_entity") + ~CaselessKeyword("by") + ~CaselessKeyword("function") + ~CaselessKeyword("based_on") + ~CaselessKeyword("from") + ~CaselessKeyword("boolean") + ~CaselessKeyword("sin") + ~CaselessKeyword("false") + ~CaselessKeyword("as") + ~CaselessKeyword("cos") + ~CaselessKeyword("else") + ~CaselessKeyword("hibound") + ~CaselessKeyword("hiindex") + ~CaselessKeyword("end_if") + ~CaselessKeyword("insert") + ~CaselessKeyword("end_type") + ~CaselessKeyword("bag") + ~CaselessKeyword("end_schema") + ~CaselessKeyword("enumeration") + ~CaselessKeyword("fixed") + ~CaselessKeyword("escape") + ~CaselessKeyword("end") + ~CaselessKeyword("div") + ~CaselessKeyword("end_procedure") + ~CaselessKeyword("blength") + ~CaselessKeyword("end_local") + ~CaselessKeyword("end_constant") + ~CaselessKeyword("end_rule") + ~CaselessKeyword("begin") + ~CaselessKeyword("lobound") + ~CaselessKeyword("constant") + ~CaselessKeyword("end_subtype_constraint") + ~CaselessKeyword("end_alias") + ~CaselessKeyword("end_case") + ~CaselessKeyword("acos") + ~CaselessKeyword("end_function") + ~CaselessKeyword("nvl") + ~CaselessKeyword("remove") + ~CaselessKeyword("oneof") + ~CaselessKeyword("renamed") + ~CaselessKeyword("if") + ~CaselessKeyword("until") + ~CaselessKeyword("true") + ~CaselessKeyword("logical") + ~CaselessKeyword("self") + ~CaselessKeyword("exp") + ~CaselessKeyword("like") + ~CaselessKeyword("real") + ~CaselessKeyword("value") + ~CaselessKeyword("end_repeat") + ~CaselessKeyword("number") + ~CaselessKeyword("local") + ~CaselessKeyword("string") + ~CaselessKeyword("to") + ~CaselessKeyword("procedure") + ~CaselessKeyword("length") + ~CaselessKeyword("subtype") + ~CaselessKeyword("select") + ~CaselessKeyword("set") + ~CaselessKeyword("tan") + ~CaselessKeyword("generic") + ~CaselessKeyword("andor") + ~CaselessKeyword("generic_entity") + ~CaselessKeyword("optional") + ~CaselessKeyword("binary") + ~CaselessKeyword("odd") + ~CaselessKeyword("for") + ~CaselessKeyword("return") + ~CaselessKeyword("total_over") + ~CaselessKeyword("usedin") + ~CaselessKeyword("value_in") + ~CaselessKeyword("format") + ~CaselessKeyword("aggregate") + ~CaselessKeyword("var") + ~CaselessKeyword("log2") + ~CaselessKeyword("reference") + ~CaselessKeyword("log") + ~CaselessKeyword("skip") + ~CaselessKeyword("sqrt") + ~CaselessKeyword("unique") + ~CaselessKeyword("inverse") + ~CaselessKeyword("where") + ~CaselessKeyword("log10") + ~CaselessKeyword("subtype_constraint") + ~CaselessKeyword("atan") + ~CaselessKeyword("rolesof") + ~CaselessKeyword("rule") + ~CaselessKeyword("in") + ~CaselessKeyword("otherwise") + ~CaselessKeyword("repeat") + ~CaselessKeyword("derive") + ~CaselessKeyword("mod") + ~CaselessKeyword("then") + ~CaselessKeyword("or") + ~CaselessKeyword("schema") + ~CaselessKeyword("list") + ~CaselessKeyword("value_unique") + ~CaselessKeyword("pi") + ~CaselessKeyword("supertype") + ~CaselessKeyword("while") + ~CaselessKeyword("const_e") + ~CaselessKeyword("alias") + ~CaselessKeyword("loindex") + ~CaselessKeyword("xor") + ~CaselessKeyword("and") + ~CaselessKeyword("entity") + ~CaselessKeyword("typeof") + ~CaselessKeyword("query") + ~CaselessKeyword("use") + ~CaselessKeyword("exists") + ~CaselessKeyword("not") + ~CaselessKeyword("integer") + ~CaselessKeyword("of") + ~CaselessKeyword("sizeof") + ~CaselessKeyword("type") + ~CaselessKeyword("unknown") + originalTextFor(Combine((letter + ZeroOrMore((letter | digit | CaselessLiteral("_"))))))
        simple_string_literal = ((CaselessLiteral("'") + ZeroOrMore(((CaselessLiteral("'") + CaselessLiteral("'")) | not_quote)) + CaselessLiteral("'")))
        abstract_entity_declaration = (ABSTRACT)
        abstract_supertype = ((ABSTRACT + SUPERTYPE + CaselessLiteral(";")))
        add_like_op = ((CaselessLiteral("+") | CaselessLiteral("-") | OR | XOR))
        attribute_id = (simple_id)
        boolean_type = (BOOLEAN)
        built_in_constant = ((CONST_E | PI | SELF | CaselessLiteral("?")))
        built_in_function = ((ABS | ACOS | ASIN | ATAN | BLENGTH | COS | EXISTS | EXP | FORMAT | HIBOUND | HIINDEX | LENGTH | LOBOUND | LOINDEX | LOG | LOG2 | LOG10 | NVL | ODD | ROLESOF | SIN | SIZEOF | SQRT | TAN | TYPEOF | USEDIN | VALUE | VALUE_IN | VALUE_UNIQUE))
        built_in_procedure = ((INSERT | REMOVE))
        constant_id = (simple_id)
        entity_id = (simple_id)
        enumeration_id = (simple_id)
        enumeration_items = ((CaselessLiteral("(") + enumeration_id + ZeroOrMore((CaselessLiteral(",") + enumeration_id)) + CaselessLiteral(")")))
        escape_stmt = ((ESCAPE + CaselessLiteral(";")))
        function_id = (simple_id)
        integer_type = (INTEGER)
        interval_op = ((CaselessLiteral("<=") | CaselessLiteral("<")))
        logical_literal = ((FALSE | TRUE | UNKNOWN))
        logical_type = (LOGICAL)
        multiplication_like_op = ((CaselessLiteral("*") | CaselessLiteral("/") | DIV | MOD | AND | CaselessLiteral("||")))
        null_stmt = (CaselessLiteral(";"))
        number_type = (NUMBER)
        parameter_id = (simple_id)
        procedure_id = (simple_id)
        rel_op = ((CaselessLiteral("<=") | CaselessLiteral(">=") | CaselessLiteral("<>") | CaselessLiteral("=") | CaselessLiteral(":<>:") | CaselessLiteral(":=:") | CaselessLiteral("<") | CaselessLiteral(">")))
        rel_op_extended = ((rel_op | IN | LIKE))
        rule_id = (simple_id)
        rule_label_id = (simple_id)
        schema_id = (simple_id)
        sign = ((CaselessLiteral("+") | CaselessLiteral("-")))
        skip_stmt = ((SKIP + CaselessLiteral(";")))
        subtype_constraint_id = (simple_id)
        type_id = (simple_id)
        type_label_id = (simple_id)
        unary_op = ((CaselessLiteral("+") | CaselessLiteral("-") | NOT))
        variable_id = (simple_id)
        encoded_character = ((octet + octet + octet + octet))
        not_paren_star = ((letter | digit | not_paren_star_special))
        not_rparen_star = ((not_paren_star | CaselessLiteral("(")))
        not_rparen_star_then_rparen = ((not_rparen_star + ZeroOrMore(not_rparen_star) + CaselessLiteral(")") + ZeroOrMore(CaselessLiteral(")"))))
        encoded_string_literal = ((CaselessLiteral("\"") + encoded_character + ZeroOrMore(encoded_character) + CaselessLiteral("\"")))
        real_literal = (((digits + CaselessLiteral(".") + Optional(digits) + Optional((CaselessLiteral("e") + Optional(sign) + digits))) | integer_literal))
        attribute_ref = (attribute_id)
        constant_ref = (constant_id)
        entity_ref = (entity_id)
        enumeration_ref = (enumeration_id)
        function_ref = (function_id)
        parameter_ref = (parameter_id)
        procedure_ref = (procedure_id)
        rule_label_ref = (rule_label_id)
        rule_ref = (rule_id)
        schema_ref = (schema_id)
        subtype_constraint_ref = (subtype_constraint_id)
        type_label_ref = (type_label_id)
        type_ref = (type_id)
        variable_ref = (variable_id)
        attribute_qualifier = ((CaselessLiteral(".") + attribute_ref))
        constant_factor = ((built_in_constant | constant_ref))
        enumeration_extension = ((BASED_ON + type_ref + Optional((WITH + enumeration_items))))
        enumeration_reference = ((Optional((type_ref + CaselessLiteral("."))) + enumeration_ref))
        enumeration_type = ((Optional(EXTENSIBLE) + ENUMERATION + Optional(((OF + enumeration_items) | enumeration_extension)))).setParseAction(lambda t: EnumerationType(t))
        general_ref = ((parameter_ref | variable_ref))
        group_qualifier = ((CaselessLiteral("\\") + entity_ref))
        named_types = ((entity_ref | type_ref))
        named_type_or_rename = ((named_types + Optional((AS + (entity_id | type_id)))))
        population = (entity_ref)
        qualified_attribute = ((SELF + group_qualifier + attribute_qualifier))
        redeclared_attribute = ((qualified_attribute + Optional((RENAMED + attribute_id))))
        referenced_attribute = ((attribute_ref | qualified_attribute))
        rename_id = ((constant_id | entity_id | function_id | procedure_id | type_id))
        resource_ref = ((constant_ref | entity_ref | function_ref | procedure_ref | type_ref))
        rule_head = ((RULE + rule_id + FOR + CaselessLiteral("(") + entity_ref + ZeroOrMore((CaselessLiteral(",") + entity_ref)) + CaselessLiteral(")") + CaselessLiteral(";")))
        select_list = ((CaselessLiteral("(") + named_types + ZeroOrMore((CaselessLiteral(",") + named_types)) + CaselessLiteral(")")))
        string_literal = ((simple_string_literal | encoded_string_literal))
        subtype_constraint_head = ((SUBTYPE_CONSTRAINT + subtype_constraint_id + FOR + entity_ref + CaselessLiteral(";")))
        subtype_declaration = ((SUBTYPE + OF + CaselessLiteral("(") + entity_ref + ZeroOrMore((CaselessLiteral(",") + entity_ref)) + CaselessLiteral(")"))).setParseAction(lambda t: SubTypeExpression(t))
        total_over = ((TOTAL_OVER + CaselessLiteral("(") + entity_ref + ZeroOrMore((CaselessLiteral(",") + entity_ref)) + CaselessLiteral(")") + CaselessLiteral(";")))
        type_label = ((type_label_id | type_label_ref))
        unique_rule = ((Optional((rule_label_id + CaselessLiteral(":"))) + referenced_attribute + ZeroOrMore((CaselessLiteral(",") + referenced_attribute))))
        use_clause = ((USE + FROM + schema_ref + Optional((CaselessLiteral("(") + named_type_or_rename + ZeroOrMore((CaselessLiteral(",") + named_type_or_rename)) + CaselessLiteral(")"))) + CaselessLiteral(";")))
        not_lparen_star = ((not_paren_star | CaselessLiteral(")")))
        remark_ref = ((attribute_ref | constant_ref | entity_ref | enumeration_ref | function_ref | parameter_ref | procedure_ref | rule_label_ref | rule_ref | schema_ref | subtype_constraint_ref | type_label_ref | type_ref | variable_ref))
        attribute_decl = ((redeclared_attribute | attribute_id))
        generic_entity_type = ((GENERIC_ENTITY + Optional((CaselessLiteral(":") + type_label))))
        generic_type = ((GENERIC + Optional((CaselessLiteral(":") + type_label))))
        literal = ((binary_literal | logical_literal | real_literal | string_literal))
        resource_or_rename = ((resource_ref + Optional((AS + rename_id))))
        schema_version_id = (string_literal)
        select_extension = ((BASED_ON + type_ref + Optional((WITH + select_list))))
        select_type = ((Optional((EXTENSIBLE + Optional(GENERIC_ENTITY))) + SELECT + Optional((select_list | select_extension)))).setParseAction(lambda t: SelectType(t))
        unique_clause = ((UNIQUE + unique_rule + CaselessLiteral(";") + ZeroOrMore((unique_rule + CaselessLiteral(";")))))
        lparen_then_not_lparen_star = ((CaselessLiteral("(") + ZeroOrMore(CaselessLiteral("(")) + not_lparen_star + ZeroOrMore(not_lparen_star)))
        remark_tag = ((CaselessLiteral("\"") + remark_ref + ZeroOrMore((CaselessLiteral(".") + remark_ref)) + CaselessLiteral("\"")))
        tail_remark = ((CaselessLiteral("--") + Optional(remark_tag)))
        constructed_types = ((enumeration_type | select_type))
        reference_clause = ((REFERENCE + FROM + schema_ref + Optional((CaselessLiteral("(") + resource_or_rename + ZeroOrMore((CaselessLiteral(",") + resource_or_rename)) + CaselessLiteral(")"))) + CaselessLiteral(";")))
        interface_specification = ((reference_clause | use_clause))
        parameter = Forward()
        qualifiable_factor = Forward()
        until_control = Forward()
        procedure_head = Forward()
        supertype_expression = Forward()
        width_spec = Forward().setParseAction(lambda t: WidthSpec(t))
        real_type = Forward()
        where_clause = Forward()
        array_type = Forward()
        stmt = Forward()
        qualifier = Forward()
        function_decl = Forward()
        index_1 = Forward()
        increment = Forward()
        repeat_control = Forward()
        term = Forward()
        instantiable_type = Forward()
        binary_type = Forward().setParseAction(lambda t: BinaryType(t))
        syntax = Forward()
        rule_decl = Forward()
        index_2 = Forward()
        general_bag_type = Forward()
        selector = Forward()
        increment_control = Forward()
        interval_high = Forward()
        entity_decl = Forward().setParseAction(lambda t: EntityDeclaration(t))
        abstract_supertype_declaration = Forward()
        entity_constructor = Forward()
        function_call = Forward()
        repeat_stmt = Forward()
        one_of = Forward()
        return_stmt = Forward()
        constant_decl = Forward()
        formal_parameter = Forward()
        subtype_constraint = Forward()
        bound_1 = Forward()
        supertype_factor = Forward()
        concrete_types = Forward()
        parameter_type = Forward()
        derive_clause = Forward().setParseAction(lambda t: AttributeList('derive', t))
        aggregate_initializer = Forward()
        index_qualifier = Forward()
        while_control = Forward()
        numeric_expression = Forward()
        compound_stmt = Forward()
        inverse_clause = Forward().setParseAction(lambda t: AttributeList('inverse', t))
        domain_rule = Forward()
        schema_decl = Forward()
        type_decl = Forward().setParseAction(lambda t: TypeDeclaration(t))
        interval_low = Forward()
        factor = Forward()
        aggregation_types = Forward().setParseAction(lambda t: AggregationType(t))
        aggregate_source = Forward()
        interval_item = Forward()
        bound_spec = Forward().setParseAction(lambda t: BoundSpecification(t))
        explicit_attr = Forward().setParseAction(lambda t: ExplicitAttribute(t))
        function_head = Forward()
        local_variable = Forward()
        expression = Forward()
        assignment_stmt = Forward()
        interval = Forward()
        repetition = Forward()
        algorithm_head = Forward()
        primary = Forward()
        general_set_type = Forward()
        subsuper = Forward()
        actual_parameter_list = Forward()
        case_stmt = Forward()
        element = Forward()
        string_type = Forward().setParseAction(lambda t: StringType(t))
        embedded_remark = Forward()
        alias_stmt = Forward()
        general_list_type = Forward()
        supertype_term = Forward()
        logical_expression = Forward()
        procedure_decl = Forward()
        constant_body = Forward()
        general_aggregation_types = Forward().setParseAction(lambda t: AggregationType(t))
        supertype_rule = Forward()
        derived_attr = Forward().setParseAction(lambda t: DerivedAttribute(t))
        case_action = Forward()
        simple_types = Forward()
        precision_spec = Forward()
        underlying_type = Forward().setParseAction(lambda t: UnderlyingType(t))
        entity_body = Forward()
        general_array_type = Forward()
        bag_type = Forward()
        entity_head = Forward()
        inverse_attr = Forward().setParseAction(lambda t: InverseAttribute(t))
        list_type = Forward()
        simple_expression = Forward()
        declaration = Forward()
        supertype_constraint = Forward().setParseAction(lambda t: SuperTypeExpression(t))
        generalized_types = Forward()
        subtype_constraint_decl = Forward()
        remark = Forward()
        width = Forward()
        simple_factor = Forward()
        query_expression = Forward()
        subtype_constraint_body = Forward()
        procedure_call_stmt = Forward()
        case_label = Forward()
        schema_body = Forward()
        if_stmt = Forward()
        index = Forward()
        set_type = Forward()
        bound_2 = Forward()
        aggregate_type = Forward()
        local_decl = Forward()
        parameter << (expression)
        qualifiable_factor << ((function_call | attribute_ref | constant_factor | general_ref | population))
        until_control << ((UNTIL + logical_expression))
        procedure_head << ((PROCEDURE + procedure_id + Optional((CaselessLiteral("(") + Optional(VAR) + formal_parameter + ZeroOrMore((CaselessLiteral(";") + Optional(VAR) + formal_parameter)) + CaselessLiteral(")"))) + CaselessLiteral(";")))
        supertype_expression << ((supertype_factor + ZeroOrMore((ANDOR + supertype_factor))))
        width_spec << ((CaselessLiteral("(") + width + CaselessLiteral(")") + Optional(FIXED)))
        real_type << ((REAL + Optional((CaselessLiteral("(") + precision_spec + CaselessLiteral(")")))))
        where_clause << ((WHERE + domain_rule + CaselessLiteral(";") + ZeroOrMore((domain_rule + CaselessLiteral(";")))))
        array_type << ((ARRAY + bound_spec + OF + Optional(OPTIONAL) + Optional(UNIQUE) + instantiable_type))
        stmt << ((alias_stmt | assignment_stmt | case_stmt | compound_stmt | escape_stmt | if_stmt | null_stmt | procedure_call_stmt | repeat_stmt | return_stmt | skip_stmt))
        qualifier << ((attribute_qualifier | group_qualifier | index_qualifier))
        function_decl << ((function_head + algorithm_head + stmt + ZeroOrMore(stmt) + END_FUNCTION + CaselessLiteral(";")))
        index_1 << (index)
        increment << (numeric_expression)
        repeat_control << ((Optional(increment_control) + Optional(while_control) + Optional(until_control)))
        term << ((factor + ZeroOrMore((multiplication_like_op + factor))))
        instantiable_type << ((concrete_types | entity_ref))
        binary_type << ((BINARY + Optional(width_spec)))
        syntax << ((schema_decl + ZeroOrMore(schema_decl)))
        rule_decl << ((rule_head + algorithm_head + ZeroOrMore(stmt) + where_clause + END_RULE + CaselessLiteral(";")))
        index_2 << (index)
        general_bag_type << ((BAG + Optional(bound_spec) + OF + parameter_type))
        selector << (expression)
        increment_control << ((variable_id + CaselessLiteral(":=") + bound_1 + TO + bound_2 + Optional((BY + increment))))
        interval_high << (simple_expression)
        entity_decl << ((entity_head + entity_body + END_ENTITY + CaselessLiteral(";")))
        abstract_supertype_declaration << ((ABSTRACT + SUPERTYPE + Optional(subtype_constraint)))
        entity_constructor << ((entity_ref + CaselessLiteral("(") + Optional((expression + ZeroOrMore((CaselessLiteral(",") + expression)))) + CaselessLiteral(")")))
        function_call << (((built_in_function | function_ref) + actual_parameter_list))
        repeat_stmt << ((REPEAT + repeat_control + CaselessLiteral(";") + stmt + ZeroOrMore(stmt) + END_REPEAT + CaselessLiteral(";")))
        one_of << ((ONEOF + CaselessLiteral("(") + supertype_expression + ZeroOrMore((CaselessLiteral(",") + supertype_expression)) + CaselessLiteral(")")))
        return_stmt << ((RETURN + Optional((CaselessLiteral("(") + expression + CaselessLiteral(")"))) + CaselessLiteral(";")))
        constant_decl << ((CONSTANT + constant_body + ZeroOrMore(constant_body) + END_CONSTANT + CaselessLiteral(";")))
        formal_parameter << ((parameter_id + ZeroOrMore((CaselessLiteral(",") + parameter_id)) + CaselessLiteral(":") + parameter_type))
        subtype_constraint << ((OF + CaselessLiteral("(") + supertype_expression + CaselessLiteral(")")))
        bound_1 << (numeric_expression)
        supertype_factor << ((supertype_term + ZeroOrMore((AND + supertype_term))))
        concrete_types << ((aggregation_types | simple_types | type_ref))
        parameter_type << ((generalized_types | simple_types | named_types))
        derive_clause << ((DERIVE + derived_attr + ZeroOrMore(derived_attr)))
        aggregate_initializer << ((CaselessLiteral("[") + Optional((element + ZeroOrMore((CaselessLiteral(",") + element)))) + CaselessLiteral("]")))
        index_qualifier << ((CaselessLiteral("[") + index_1 + Optional((CaselessLiteral(":") + index_2)) + CaselessLiteral("]")))
        while_control << ((WHILE + logical_expression))
        numeric_expression << (simple_expression)
        compound_stmt << ((BEGIN + stmt + ZeroOrMore(stmt) + END + CaselessLiteral(";")))
        inverse_clause << ((INVERSE + inverse_attr + ZeroOrMore(inverse_attr)))
        domain_rule << ((Optional((rule_label_id + CaselessLiteral(":"))) + expression))
        schema_decl << ((SCHEMA + schema_id + Optional(schema_version_id) + CaselessLiteral(";") + schema_body + END_SCHEMA + CaselessLiteral(";")))
        type_decl << ((TYPE + type_id + CaselessLiteral("=") + underlying_type + CaselessLiteral(";") + Optional(where_clause) + END_TYPE + CaselessLiteral(";")))
        interval_low << (simple_expression)
        factor << ((simple_factor + Optional((CaselessLiteral("**") + simple_factor))))
        aggregation_types << ((array_type | bag_type | list_type | set_type))
        aggregate_source << (simple_expression)
        interval_item << (simple_expression)
        bound_spec << ((CaselessLiteral("[") + bound_1 + CaselessLiteral(":") + bound_2 + CaselessLiteral("]")))
        explicit_attr << ((attribute_decl + ZeroOrMore((CaselessLiteral(",") + attribute_decl)) + CaselessLiteral(":") + Optional(OPTIONAL) + parameter_type + CaselessLiteral(";")))
        function_head << ((FUNCTION + function_id + Optional((CaselessLiteral("(") + formal_parameter + ZeroOrMore((CaselessLiteral(";") + formal_parameter)) + CaselessLiteral(")"))) + CaselessLiteral(":") + parameter_type + CaselessLiteral(";")))
        local_variable << ((variable_id + ZeroOrMore((CaselessLiteral(",") + variable_id)) + CaselessLiteral(":") + parameter_type + Optional((CaselessLiteral(":=") + expression)) + CaselessLiteral(";")))
        expression << ((simple_expression + Optional((rel_op_extended + simple_expression))))
        assignment_stmt << ((general_ref + ZeroOrMore(qualifier) + CaselessLiteral(":=") + expression + CaselessLiteral(";")))
        interval << ((CaselessLiteral("{") + interval_low + interval_op + interval_item + interval_op + interval_high + CaselessLiteral("}")))
        repetition << (numeric_expression)
        algorithm_head << ((ZeroOrMore(declaration) + Optional(constant_decl) + Optional(local_decl)))
        primary << ((literal | (qualifiable_factor + ZeroOrMore(qualifier))))
        general_set_type << ((SET + Optional(bound_spec) + OF + parameter_type))
        subsuper << ((Optional(supertype_constraint) + Optional(subtype_declaration)))
        actual_parameter_list << ((CaselessLiteral("(") + Optional(parameter) + ZeroOrMore((CaselessLiteral(",") + parameter)) + CaselessLiteral(")")))
        case_stmt << ((CASE + selector + OF + ZeroOrMore(case_action) + Optional((OTHERWISE + CaselessLiteral(":") + stmt)) + END_CASE + CaselessLiteral(";")))
        element << ((expression + Optional((CaselessLiteral(":") + repetition))))
        string_type << ((STRING + Optional(width_spec)))
        embedded_remark << ((CaselessLiteral("(*") + Optional(remark_tag) + ZeroOrMore(((not_paren_star + ZeroOrMore(not_paren_star)) | lparen_then_not_lparen_star | (CaselessLiteral("*") + ZeroOrMore(CaselessLiteral("*"))) | not_rparen_star_then_rparen | embedded_remark)) + CaselessLiteral("*)")))
        alias_stmt << ((ALIAS + variable_id + FOR + general_ref + ZeroOrMore(qualifier) + CaselessLiteral(";") + stmt + ZeroOrMore(stmt) + END_ALIAS + CaselessLiteral(";")))
        general_list_type << ((LIST + Optional(bound_spec) + OF + Optional(UNIQUE) + parameter_type))
        supertype_term << ((one_of | (CaselessLiteral("(") + supertype_expression + CaselessLiteral(")")) | entity_ref))
        logical_expression << (expression)
        procedure_decl << ((procedure_head + algorithm_head + ZeroOrMore(stmt) + END_PROCEDURE + CaselessLiteral(";")))
        constant_body << ((constant_id + CaselessLiteral(":") + instantiable_type + CaselessLiteral(":=") + expression + CaselessLiteral(";")))
        general_aggregation_types << ((general_array_type | general_bag_type | general_list_type | general_set_type))
        supertype_rule << ((SUPERTYPE + subtype_constraint))
        derived_attr << ((attribute_decl + CaselessLiteral(":") + parameter_type + CaselessLiteral(":=") + expression + CaselessLiteral(";")))
        case_action << ((case_label + ZeroOrMore((CaselessLiteral(",") + case_label)) + CaselessLiteral(":") + stmt))
        simple_types << ((binary_type | boolean_type | integer_type | logical_type | number_type | real_type | string_type))
        precision_spec << (numeric_expression)
        underlying_type << ((constructed_types | concrete_types))
        entity_body << ((ZeroOrMore(explicit_attr) + Optional(derive_clause) + Optional(inverse_clause) + Optional(unique_clause) + Optional(where_clause)))
        general_array_type << ((ARRAY + Optional(bound_spec) + OF + Optional(OPTIONAL) + Optional(UNIQUE) + parameter_type))
        bag_type << ((BAG + Optional(bound_spec) + OF + instantiable_type))
        entity_head << ((ENTITY + entity_id + subsuper + CaselessLiteral(";")))
        inverse_attr << ((attribute_decl + CaselessLiteral(":") + Optional(((SET | BAG) + Optional(bound_spec) + OF)) + entity_ref + FOR + Optional((entity_ref + CaselessLiteral("."))) + attribute_ref + CaselessLiteral(";")))
        list_type << ((LIST + Optional(bound_spec) + OF + Optional(UNIQUE) + instantiable_type))
        simple_expression << ((term + ZeroOrMore((add_like_op + term))))
        declaration << ((entity_decl | function_decl | procedure_decl | subtype_constraint_decl | type_decl))
        supertype_constraint << ((abstract_supertype_declaration | abstract_entity_declaration | supertype_rule))
        generalized_types << ((aggregate_type | general_aggregation_types | generic_entity_type | generic_type))
        subtype_constraint_decl << ((subtype_constraint_head + subtype_constraint_body + END_SUBTYPE_CONSTRAINT + CaselessLiteral(";")))
        remark << ((embedded_remark | tail_remark))
        width << (numeric_expression)
        simple_factor << ((aggregate_initializer | interval | query_expression | (Optional(unary_op) + ((CaselessLiteral("(") + expression + CaselessLiteral(")")) | primary)) | entity_constructor | enumeration_reference))
        query_expression << ((QUERY + CaselessLiteral("(") + variable_id + CaselessLiteral("<*") + aggregate_source + CaselessLiteral("|") + logical_expression + CaselessLiteral(")")))
        subtype_constraint_body << ((Optional(abstract_supertype) + Optional(total_over) + Optional((supertype_expression + CaselessLiteral(";")))))
        procedure_call_stmt << (((built_in_procedure | procedure_ref) + actual_parameter_list + CaselessLiteral(";")))
        case_label << (expression)
        schema_body << ((ZeroOrMore(interface_specification) + Optional(constant_decl) + ZeroOrMore((declaration | rule_decl))))
        if_stmt << ((IF + logical_expression + THEN + stmt + ZeroOrMore(stmt) + Optional((ELSE + stmt + ZeroOrMore(stmt))) + END_IF + CaselessLiteral(";")))
        index << (numeric_expression)
        set_type << ((SET + Optional(bound_spec) + OF + instantiable_type))
        bound_2 << (numeric_expression)
        aggregate_type << ((AGGREGATE + Optional((CaselessLiteral(":") + type_label)) + OF + parameter_type))
        local_decl << ((LOCAL + local_variable + ZeroOrMore(local_variable) + END_LOCAL + CaselessLiteral(";")))

        syntax.ignore("--" + restOfLine)
        syntax.ignore(Regex(r"\((?:\*(?:[^*]*\*+)+?\))"))
        ast = syntax.parseFile(fn)
        s = schema.Schema(ast)

        with open(cache_file, "wb") as f:
            pickle.dump(s, f, protocol=0)    

    return s