if __name__ == '__main__':
    import sys
    conf = {
      "sqs-queue-name": sys.argv[1],
      "sqs-region": "us-east-1",
      "sqs-path": "sqssend"
    }

    import boto.sqs
    conn = boto.sqs.connect_to_region(conf.get('sqs-region'))
    q = conn.get_queue(conf.get('sqs-queue-name'))

    import time
    while(True):
            for m in q.get_messages():
                    print '%s: %s' % (m, m.get_body())
                    q.delete_message(m)
            time.sleep(1)
