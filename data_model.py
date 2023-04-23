#Of course, this precise specification of the meaning of the return value of each method is not defined in the diagram itself, but it accompanies somehow the descriptive diagram as a natural language description of what the method should do. However, the diagram already provides the means of the kinds of input and the related output each method must to take and provide, respectively.


class IdentifiableEntity(object):
    def __init__(self, id) -> None:
        self.id = id 

    def getId(self) -> str:
        return self.id

class Image(IdentifiableEntity):
    pass

class Annotation(IdentifiableEntity):
    def __init__(self, motivation, target, body) -> None:
        self.motivation = motivation
        self.target = target
        self.body = body

    def getBody(self) -> Image:
        return self.body

    def getMotivation(self) -> str:
        return self.motivation

    def getTarget(self) -> IdentifiableEntity:
        return self.target

class EntityWithMetadata(IdentifiableEntity):
    def __init__(self, id, label:str, title:str, creators:str) -> None:
        self.label = label
        self.title = title
        self.creators = set()
        for creator in creators:
            self.creators.add(creator)

        super().__init__(id)

    def getLabel(self) -> str:
        return self.label

    def getTitle(self) -> str: #(or None)
        return self.title

    def getCreators(self) -> list[str]:
        result = list()
        for creator in self.creators:
            result.append(creator)
        result.sort()
        return result 

class Canvas(EntityWithMetadata):
    def __init__(self, id) -> None:
        super().__init__(id)

class Manifest(EntityWithMetadata):
    def __init__(self, id, items) -> None:
        self.items = set()
        for item in items:
            self.items.add(item)

        super().__init__(id)

    def getItems(self) -> list[Canvas]:
        result = list()
        for item in self.items: 
            result.append(item)
        result.sort()
        return result

class Collection(EntityWithMetadata):
    def __init__(self, id, items) -> None:
        self.items = set()
        for item in items:
            self.items.add(item)

        super().__init__(id)

    def getItems(self) -> list[Manifest]:
        result = list()
        for item in self.items: 
            result.append(item)
        result.sort()
        return result