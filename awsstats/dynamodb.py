from awsstats import utils

__all__ = ('get_avg_read_capacity',
           'get_avg_write_capacity',)


def get_avg_read_capacity(table_name):
    '''
    Units: Count
    '''

    args = utils.get_metric_stats_args(utils.DDB_NAMESPACE,
                                       'ConsumedReadCapacityUnits',
                                       ('TableName', table_name))
    return utils.fetch_stats(args)


def get_avg_write_capacity(table_name):
    '''
    Units: Count
    '''

    args = utils.get_metric_stats_args(utils.DDB_NAMESPACE,
                                       'ConsumedWriteCapacityUnits',
                                       ('TableName', table_name))

    return utils.fetch_stats(args)
