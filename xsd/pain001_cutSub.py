#!/usr/bin/env python

#
# Generated Tue Mar 22 11:56:52 2016 by generateDS.py version 2.20a.
#
# Command line options:
#   ('-o', 'pain001_cut.py')
#   ('-s', 'pain001_cutSub.py')
#   ('--super', 'pain001_cut')
#   ('--member-specs', 'dict')
#   ('--export', 'write etree')
#
# Command line arguments:
#   pain_cutted.xsd
#
# Command line:
#   c:\Python27\Scripts\generateDS.py -o "pain001_cut.py" -s "pain001_cutSub.py" --super="pain001_cut" --member-specs="dict" --export="write etree" pain_cutted.xsd
#
# Current working directory (os.getcwd()):
#   xsd
#

import sys
from lxml import etree as etree_

import pain001_cut as supermod

def parsexml_(infile, parser=None, **kwargs):
    if parser is None:
        # Use the lxml ElementTree compatible parser so that, e.g.,
        #   we ignore comments.
        parser = etree_.ETCompatXMLParser()
    doc = etree_.parse(infile, parser=parser, **kwargs)
    return doc

#
# Globals
#

ExternalEncoding = 'ascii'

#
# Data representation classes
#


class DocumentSub(supermod.Document):
    def __init__(self, CstmrCdtTrfInitn=None):
        super(DocumentSub, self).__init__(CstmrCdtTrfInitn, )
supermod.Document.subclass = DocumentSub
# end class DocumentSub


class CustomerCreditTransferInitiationV03_CHSub(supermod.CustomerCreditTransferInitiationV03_CH):
    def __init__(self, GrpHdr=None, PmtInf=None):
        super(CustomerCreditTransferInitiationV03_CHSub, self).__init__(GrpHdr, PmtInf, )
supermod.CustomerCreditTransferInitiationV03_CH.subclass = CustomerCreditTransferInitiationV03_CHSub
# end class CustomerCreditTransferInitiationV03_CHSub


class PaymentInstructionInformation3_CHSub(supermod.PaymentInstructionInformation3_CH):
    def __init__(self, PmtInfId=None, PmtMtd=None, BtchBookg=None, NbOfTxs=None, CtrlSum=None, PmtTpInf=None, ReqdExctnDt=None, Dbtr=None, DbtrAcct=None, DbtrAgt=None, UltmtDbtr=None, ChrgBr=None, ChrgsAcct=None, CdtTrfTxInf=None):
        super(PaymentInstructionInformation3_CHSub, self).__init__(PmtInfId, PmtMtd, BtchBookg, NbOfTxs, CtrlSum, PmtTpInf, ReqdExctnDt, Dbtr, DbtrAcct, DbtrAgt, UltmtDbtr, ChrgBr, ChrgsAcct, CdtTrfTxInf, )
supermod.PaymentInstructionInformation3_CH.subclass = PaymentInstructionInformation3_CHSub
# end class PaymentInstructionInformation3_CHSub


class GroupHeader32_CHSub(supermod.GroupHeader32_CH):
    def __init__(self, MsgId=None, CreDtTm=None, NbOfTxs=None, CtrlSum=None, InitgPty=None, FwdgAgt=None):
        super(GroupHeader32_CHSub, self).__init__(MsgId, CreDtTm, NbOfTxs, CtrlSum, InitgPty, FwdgAgt, )
supermod.GroupHeader32_CH.subclass = GroupHeader32_CHSub
# end class GroupHeader32_CHSub


class PartyIdentification32_CH_NameAndIdSub(supermod.PartyIdentification32_CH_NameAndId):
    def __init__(self, Nm=None, Id=None, CtctDtls=None):
        super(PartyIdentification32_CH_NameAndIdSub, self).__init__(Nm, Id, CtctDtls, )
supermod.PartyIdentification32_CH_NameAndId.subclass = PartyIdentification32_CH_NameAndIdSub
# end class PartyIdentification32_CH_NameAndIdSub


class Party6Choice_CHSub(supermod.Party6Choice_CH):
    def __init__(self, OrgId=None, PrvtId=None):
        super(Party6Choice_CHSub, self).__init__(OrgId, PrvtId, )
supermod.Party6Choice_CH.subclass = Party6Choice_CHSub
# end class Party6Choice_CHSub


class ContactDetails2_CHSub(supermod.ContactDetails2_CH):
    def __init__(self, Nm=None, Othr=None):
        super(ContactDetails2_CHSub, self).__init__(Nm, Othr, )
supermod.ContactDetails2_CH.subclass = ContactDetails2_CHSub
# end class ContactDetails2_CHSub


class OrganisationIdentification4_CHSub(supermod.OrganisationIdentification4_CH):
    def __init__(self, BICOrBEI=None, Othr=None):
        super(OrganisationIdentification4_CHSub, self).__init__(BICOrBEI, Othr, )
supermod.OrganisationIdentification4_CH.subclass = OrganisationIdentification4_CHSub
# end class OrganisationIdentification4_CHSub


class PersonIdentification5_CHSub(supermod.PersonIdentification5_CH):
    def __init__(self, DtAndPlcOfBirth=None, Othr=None):
        super(PersonIdentification5_CHSub, self).__init__(DtAndPlcOfBirth, Othr, )
supermod.PersonIdentification5_CH.subclass = PersonIdentification5_CHSub
# end class PersonIdentification5_CHSub


class DateAndPlaceOfBirthSub(supermod.DateAndPlaceOfBirth):
    def __init__(self, BirthDt=None, PrvcOfBirth=None, CityOfBirth=None, CtryOfBirth=None):
        super(DateAndPlaceOfBirthSub, self).__init__(BirthDt, PrvcOfBirth, CityOfBirth, CtryOfBirth, )
supermod.DateAndPlaceOfBirth.subclass = DateAndPlaceOfBirthSub
# end class DateAndPlaceOfBirthSub


def get_root_tag(node):
    tag = supermod.Tag_pattern_.match(node.tag).groups()[-1]
    rootClass = None
    rootClass = supermod.GDSClassesMapping.get(tag)
    if rootClass is None and hasattr(supermod, tag):
        rootClass = getattr(supermod, tag)
    return tag, rootClass


def parse(inFilename, silence=False):
    parser = None
    doc = parsexml_(inFilename, parser)
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'Document'
        rootClass = supermod.Document
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    doc = None
    if not silence:
        sys.stdout.write('<?xml version="1.0" ?>\n')
        rootObj.export(
            sys.stdout, 0, name_=rootTag,
            namespacedef_='',
            pretty_print=True)
    return rootObj


def parseEtree(inFilename, silence=False):
    parser = None
    doc = parsexml_(inFilename, parser)
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'Document'
        rootClass = supermod.Document
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    doc = None
    mapping = {}
    rootElement = rootObj.to_etree(None, name_=rootTag, mapping_=mapping)
    reverse_mapping = rootObj.gds_reverse_node_mapping(mapping)
    if not silence:
        content = etree_.tostring(
            rootElement, pretty_print=True,
            xml_declaration=True, encoding="utf-8")
        sys.stdout.write(content)
        sys.stdout.write('\n')
    return rootObj, rootElement, mapping, reverse_mapping


def parseString(inString, silence=False):
    from StringIO import StringIO
    parser = None
    doc = parsexml_(StringIO(inString), parser)
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'Document'
        rootClass = supermod.Document
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    doc = None
    if not silence:
        sys.stdout.write('<?xml version="1.0" ?>\n')
        rootObj.export(
            sys.stdout, 0, name_=rootTag,
            namespacedef_='')
    return rootObj


def parseLiteral(inFilename, silence=False):
    parser = None
    doc = parsexml_(inFilename, parser)
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'Document'
        rootClass = supermod.Document
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    doc = None
    if not silence:
        sys.stdout.write('#from pain001_cut import *\n\n')
        sys.stdout.write('import pain001_cut as model_\n\n')
        sys.stdout.write('rootObj = model_.rootClass(\n')
        rootObj.exportLiteral(sys.stdout, 0, name_=rootTag)
        sys.stdout.write(')\n')
    return rootObj


USAGE_TEXT = """
Usage: python ???.py <infilename>
"""


def usage():
    print(USAGE_TEXT)
    sys.exit(1)


def main():
    args = sys.argv[1:]
    if len(args) != 1:
        usage()
    infilename = args[0]
    parse(infilename)


if __name__ == '__main__':
    #import pdb; pdb.set_trace()
    main()
